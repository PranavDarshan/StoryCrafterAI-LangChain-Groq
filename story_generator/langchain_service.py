import logging
import os
import requests
import json
import time
from langchain.llms.base import LLM
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.callbacks.manager import CallbackManagerForLLMRun
from typing import Optional, List, Any
from dotenv import load_dotenv
import warnings
warnings.filterwarnings("ignore")

# Load environment variables from .env file
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class GroqLLM(LLM):
    """Custom LangChain LLM wrapper for Groq API"""
    
    groq_api_key: str
    model_name: str = "llama-3.3-70b-versatile"  # Updated to current model
    temperature: float = 0.8
    max_tokens: int = 1000
    
    def __init__(self, groq_api_key: str, model_name: str = "llama-3.3-70b-versatile", **kwargs):
        super().__init__(
        groq_api_key=groq_api_key,
        model_name=model_name,
        **kwargs
    )
    
    @property
    def _llm_type(self) -> str:
        return "groq"
    
    def _call(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> str:
        """Call Groq API"""
        try:
            headers = {
                'Authorization': f'Bearer {self.groq_api_key}',
                'Content-Type': 'application/json'
            }
            
            messages = [
                {
                    "role": "system", 
                    "content": "You are a creative storyteller. Generate engaging, family-friendly content based on user prompts. Be descriptive and imaginative."
                },
                {
                    "role": "user", 
                    "content": prompt
                }
            ]
            
            data = {
                'model': self.model_name,
                'messages': messages,
                'max_tokens': kwargs.get('max_tokens', self.max_tokens),
                'temperature': kwargs.get('temperature', self.temperature),
                'top_p': 0.9,
                'stream': False
            }
            
            response = requests.post(
                'https://api.groq.com/openai/v1/chat/completions',
                headers=headers,
                json=data,
                timeout=60
            )
            
            if response.status_code == 200:
                result = response.json()
                content = result['choices'][0]['message']['content']
                
                # Log token usage if available
                if 'usage' in result:
                    usage = result['usage']
                    logger.info(f"Tokens used: {usage.get('total_tokens', 'N/A')} (prompt: {usage.get('prompt_tokens', 'N/A')}, completion: {usage.get('completion_tokens', 'N/A')})")
                
                return content.strip()
            
            elif response.status_code == 429:
                logger.warning("Groq API rate limit reached, waiting...")
                time.sleep(2)
                raise Exception("Rate limit exceeded")
            
            elif response.status_code == 401:
                raise Exception("Invalid Groq API key")
            
            else:
                raise Exception(f"Groq API error: {response.status_code} - {response.text}")
                
        except requests.exceptions.Timeout:
            raise Exception("Groq API timeout")
        except Exception as e:
            logger.error(f"Groq API call failed: {e}")
            raise e

class StoryGenerationService:
    def __init__(self, groq_api_key=None):
        """
        Initialize Story Generation Service with Groq API only
        
        Args:
            groq_api_key (str): Your Groq API key. If None, will try to load from .env file
        """
        # Load API key from .env file if not provided
        self.groq_api_key = groq_api_key or os.getenv('GROQ_API_KEY')
        
        if not self.groq_api_key:
            raise ValueError(
                "Groq API key is required. Please provide it either:\n"
                "1. As a parameter: StoryGenerationService(groq_api_key='your_key')\n"
                "2. In a .env file: GROQ_API_KEY=your_key\n"
                "Get your API key from: https://console.groq.com/"
            )
        
        # Updated Groq model configurations based on current available models (August 2025)
        self.groq_models = {
            'llama-3.3-70b-versatile': {
                'max_tokens': 32768,
                'context_window': 131072,  # 128k context
                'description': 'Latest Llama 3.3 70B - Best for creative writing and complex tasks',
                'temperature': 0.8
            },
            'llama-3.1-8b-instant': {
                'max_tokens': 131072,
                'context_window': 131072,  # 128k context
                'description': 'Fast Llama 3.1 8B - Good balance of speed and quality',
                'temperature': 0.8
            },
            'gemma2-9b-it': {
                'max_tokens': 8192,
                'context_window': 8192,
                'description': 'Google Gemma2 9B - Reliable for creative tasks',
                'temperature': 0.8
            },
            # Preview models (use with caution in production)
            'deepseek-r1-distill-llama-70b': {
                'max_tokens': 131072,
                'context_window': 131072,
                'description': 'DeepSeek R1 70B - Advanced reasoning capabilities (Preview)',
                'temperature': 0.8
            },
            'qwen/qwen3-32b': {
                'max_tokens': 40960,
                'context_window': 131072,
                'description': 'Qwen 3 32B - Multilingual support with strong reasoning (Preview)',
                'temperature': 0.8
            }
        }
        
        self.current_model = 'llama-3.3-70b-versatile'  # Default to best production model
        
        # Initialize LangChain LLM
        self.llm = self._initialize_groq_llm()
        
        logger.info("Story Generation Service initialized with Groq API")
        self._test_groq_connection()
    
    def _initialize_groq_llm(self):
        """Initialize Groq LLM for LangChain"""
        return GroqLLM(
            groq_api_key=self.groq_api_key,
            model_name=self.current_model,
            temperature=0.8,
            max_tokens=1000
        )
    
    def _test_groq_connection(self):
        """Test Groq API connection and find best available model"""
        # Try production models first, then preview models
        production_models = ['llama-3.3-70b-versatile', 'llama-3.1-8b-instant', 'gemma2-9b-it']
        preview_models = ['deepseek-r1-distill-llama-70b', 'qwen/qwen3-32b']
        
        all_models = production_models + preview_models
        
        for model in all_models:
            try:
                # Create test LLM with current model
                test_llm = GroqLLM(
                    groq_api_key=self.groq_api_key,
                    model_name=model,
                    max_tokens=10
                )
                
                # Test with a simple prompt
                response = test_llm._call("Test connection", max_tokens=10)
                if response:
                    self.current_model = model
                    # Update main LLM with working model
                    self.llm = GroqLLM(
                        groq_api_key=self.groq_api_key,
                        model_name=model,
                        temperature=0.8,
                        max_tokens=1000
                    )
                    model_type = "Production" if model in production_models else "Preview"
                    logger.info(f"Groq API connected successfully using {model_type} model: {model}")
                    logger.info(f"Model specs: {self.groq_models[model]['description']}")
                    
                    if model in preview_models:
                        logger.warning(f"Using preview model {model}. Not recommended for production use.")
                    
                    return True
            except Exception as e:
                logger.warning(f"Model {model} failed: {e}")
                continue
        
        raise Exception("All Groq models failed. Please check your API key and internet connection.")
    
    def set_model(self, model_name):
        """Manually set a specific model"""
        if model_name not in self.groq_models:
            available_models = list(self.groq_models.keys())
            raise ValueError(f"Model {model_name} not available. Choose from: {available_models}")
        
        try:
            # Test the model first
            test_llm = GroqLLM(
                groq_api_key=self.groq_api_key,
                model_name=model_name,
                max_tokens=10
            )
            test_response = test_llm._call("Test", max_tokens=10)
            
            if test_response:
                self.current_model = model_name
                self.llm = GroqLLM(
                    groq_api_key=self.groq_api_key,
                    model_name=model_name,
                    temperature=0.8,
                    max_tokens=1000
                )
                logger.info(f"Successfully switched to model: {model_name}")
                return True
            else:
                raise Exception("Model test failed")
                
        except Exception as e:
            logger.error(f"Failed to set model {model_name}: {e}")
            raise e
    
    def list_available_models(self):
        """List all available models with their descriptions"""
        production_models = {}
        preview_models = {}
        
        for model, specs in self.groq_models.items():
            if model in ['llama-3.3-70b-versatile', 'llama-3.1-8b-instant', 'gemma2-9b-it']:
                production_models[model] = specs
            else:
                preview_models[model] = specs
        
        return {
            'production_models': production_models,
            'preview_models': preview_models,
            'current_model': self.current_model
        }
    
    def generate_story_and_descriptions(self, user_prompt):
        """Generate story with character and background descriptions using Groq AI with LangChain"""
        try:
            logger.info("Starting story generation...")
            
            # Generate story using LangChain
            story = self._generate_story(user_prompt)
            logger.info("Story generated")
            
            # Generate character description using LangChain
            character_desc = self._generate_character_description(story, user_prompt)
            logger.info("Character description generated")
            
            # Generate background description using LangChain
            background_desc = self._generate_background_description(story, user_prompt)
            logger.info("Background description generated")
            
            return {
                'story': story,
                'character_description': character_desc,
                'background_description': background_desc,
                'model_used': f"groq-{self.current_model}",
                'groq_model_info': self.groq_models.get(self.current_model)
            }
            
        except Exception as e:
            logger.error(f"Error in story generation: {e}")
            raise e
    
    def _generate_story(self, user_prompt):
        """Generate story using LangChain with Groq"""
        story_template = """Write a creative short story (3-4 paragraphs) based on this prompt:

Prompt: {user_prompt}

Requirements:
- Create vivid, engaging characters
- Build an immersive setting with rich details
- Include conflict and resolution
- Use descriptive language that brings the scene to life
- Keep it family-friendly but compelling
- Make it between 200-400 words

Story:"""
        
        try:
            prompt = PromptTemplate(
                input_variables=["user_prompt"],
                template=story_template
            )
            
            # Create LangChain chain
            chain = LLMChain(llm=self.llm, prompt=prompt)
            result = chain.run(user_prompt=user_prompt)
            
            return self._clean_generated_text(result)
            
        except Exception as e:
            logger.error(f"Error generating story: {e}")
            raise e
    
    def _generate_character_description(self, story, user_prompt):
        """Generate character description using LangChain with Groq"""
        char_template = """Based on this story, create a detailed character description for visual art creation:

Story: {story}

Create a comprehensive character description including:
- Physical appearance (age, build, facial features, hair, eyes)
- Clothing and accessories (style, colors, materials, details)
- Facial expression and emotional state
- Body posture and pose
- Distinctive features or characteristics
- Overall aesthetic and style

Focus on visual details that would help an artist create a compelling character illustration.

Character description:"""
        
        try:
            prompt = PromptTemplate(
                input_variables=["story"],
                template=char_template
            )
            
            # Create LangChain chain
            chain = LLMChain(llm=self.llm, prompt=prompt)
            result = chain.run(story=story)
            
            return self._clean_generated_text(result)
            
        except Exception as e:
            logger.error(f"Error generating character description: {e}")
            raise e
    
    def _generate_background_description(self, story, user_prompt):
        """Generate background description using LangChain with Groq"""
        bg_template = """Based on this story, create a detailed background/setting description for visual art creation:

Story: {story}

Create a comprehensive setting description including:
- Location and environment type (indoor/outdoor, natural/urban, etc.)
- Architectural or natural features and details
- Time of day, weather, and seasonal elements
- Lighting conditions and atmospheric effects
- Colors, textures, and materials visible in the scene
- Mood and atmosphere of the setting
- Any magical or fantastical elements if applicable

Focus on visual details that would help an artist create a compelling background painting.

Background description:"""
        
        try:
            prompt = PromptTemplate(
                input_variables=["story"],
                template=bg_template
            )
            
            # Create LangChain chain
            chain = LLMChain(llm=self.llm, prompt=prompt)
            result = chain.run(story=story)
            
            return self._clean_generated_text(result)
            
        except Exception as e:
            logger.error(f"Error generating background description: {e}")
            raise e
    
    def _clean_generated_text(self, text):
        """Clean and improve generated text"""
        if not text:
            return ""
        
        # Remove common prefixes
        prefixes_to_remove = [
            "Story:", "Character description:", "Background description:",
            "Character:", "Background:", "Setting:", "Description:",
            "Based on the story,", "Here is", "Here's", "The story"
        ]
        
        cleaned = text.strip()
        for prefix in prefixes_to_remove:
            if cleaned.startswith(prefix):
                cleaned = cleaned[len(prefix):].strip()
        
        # Remove repetitive sentences
        sentences = [s.strip() for s in cleaned.split('.') if s.strip()]
        unique_sentences = []
        
        for sentence in sentences:
            if sentence and len(sentence) > 10:
                # Check if this sentence is too similar to previous ones
                is_duplicate = False
                for prev_sentence in unique_sentences[-2:]:  # Check last 2 sentences
                    if self._sentences_similar(sentence, prev_sentence):
                        is_duplicate = True
                        break
                
                if not is_duplicate:
                    unique_sentences.append(sentence)
        
        return '. '.join(unique_sentences) + '.' if unique_sentences else cleaned
    
    def _sentences_similar(self, sent1, sent2, threshold=0.7):
        """Check if two sentences are too similar"""
        words1 = set(sent1.lower().split())
        words2 = set(sent2.lower().split())
        
        if len(words1) == 0 or len(words2) == 0:
            return False
        
        intersection = len(words1.intersection(words2))
        union = len(words1.union(words2))
        
        return intersection / union > threshold
    
    def create_image_prompts(self, character_desc, background_desc):
        """Create optimized prompts for Stable Diffusion"""
        # Optimize character prompt for image generation
        character_prompt = f"{character_desc}, portrait, detailed, high quality, digital art, fantasy style, concept art"
        
        # Optimize background prompt  
        background_prompt = f"{background_desc}, landscape, detailed, high quality, digital art, fantasy style, matte painting"
        
        # Clean and limit prompts
        character_prompt = self._clean_prompt(character_prompt)[:300]
        background_prompt = self._clean_prompt(background_prompt)[:300]
        
        return {
            'character_prompt': character_prompt,
            'background_prompt': background_prompt
        }
    
    def _clean_prompt(self, prompt):
        """Clean prompt for image generation"""
        # Remove problematic words/phrases
        removals = ['describe', 'description:', 'character:', 'background:', 'story:', '\n']
        cleaned = prompt.lower()
        for removal in removals:
            cleaned = cleaned.replace(removal, '')
        
        # Add positive keywords
        if 'portrait' not in cleaned and 'landscape' not in cleaned:
            cleaned = f"beautiful {cleaned}"
        
        return cleaned.strip()
    
    def get_model_info(self):
        """Get information about the current model being used"""
        model_type = "Production"
        if self.current_model in ['deepseek-r1-distill-llama-70b', 'qwen/qwen3-32b']:
            model_type = "Preview"
        
        return {
            'provider': 'Groq',
            'model': self.current_model,
            'model_type': model_type,
            'specs': self.groq_models[self.current_model],
            'api_status': 'active',
            'langchain_integration': True
        }

# Usage example:
"""
# Method 1: Initialize with API key directly
service = StoryGenerationService(groq_api_key="your_groq_api_key_here")

# Method 2: Initialize with .env file
# Create a .env file with: GROQ_API_KEY=your_groq_api_key_here
service = StoryGenerationService()

# List available models
models = service.list_available_models()
print("Production Models:", list(models['production_models'].keys()))
print("Preview Models:", list(models['preview_models'].keys()))
print("Current Model:", models['current_model'])

# Optionally set a specific model
# service.set_model('llama-3.1-8b-instant')  # For faster responses
# service.set_model('deepseek-r1-distill-llama-70b')  # For advanced reasoning

# Generate story using LangChain chains
result = service.generate_story_and_descriptions("a magical forest adventure")

# Check what model was used
model_info = service.get_model_info()
print(f"Using: {model_info['provider']} - {model_info['model']} ({model_info['model_type']}) with LangChain: {model_info['langchain_integration']}")

# Print results
print("Story:", result['story'])
print("Character:", result['character_description'])
print("Background:", result['background_description'])

# Create image prompts
image_prompts = service.create_image_prompts(
    result['character_description'], 
    result['background_description']
)
print("Character Prompt:", image_prompts['character_prompt'])
print("Background Prompt:", image_prompts['background_prompt'])
"""