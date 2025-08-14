# Creative Story Generator

This Django-based web application generates creative stories with accompanying images and audio transcriptions. Users can provide a prompt, and the application will generate a story, a character description, and a background description. It then uses these descriptions to generate images and combines them. The application also supports audio input, which is transcribed to text and used as a prompt.

## Features

-   **Story Generation:** Generates a short story based on a user prompt.
-   **Image Generation:** Creates a character image and a background image based on the generated story.
-   **Image Combination:** Combines the character and background images into a single image.
-   **Audio Transcription:** Transcribes user-uploaded audio into text to be used as a prompt.
-   **Model Details:** The application uses several AI models for its functionalities.

## Screenshots

**Dashboard**
![Dashboard](assets/dashboard-story.png)

**Entering a Prompt**
![Entering a Prompt](assets/prompt-enter-dashboard.png)

**Generated Story and Image**
![Generated Story and Image](assets/image-generated.png)

**Prompt Details**
![Prompt Details](assets/prompt-details.png)

## Models Used

### Story Generation

-   **Service:** `story_generator/langchain_service.py`
-   **Provider:** Groq API
-   **Default Model:** `llama-3.3-70b-versatile`
-   **Other Production Models:** `llama-3.1-8b-instant`, `gemma2-9b-it`
-   **Preview Models:** `deepseek-r1-distill-llama-70b`, `qwen/qwen3-32b`

### Image Generation

-   **Service:** `story_generator/image_service.py`
-   **Primary Model:** `CompVis/stable-diffusion-v1-4`
-   **Fallback Model:** `nota-ai/bk-sdm-small` (used if the primary model fails)

### Audio Transcription

-   **Service:** `story_generator/audio_service.py`
-   **Model:** `whisper-tiny`

## Getting Started

### Prerequisites

-   Python 3.10+
-   Django
-   Groq API Key

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/PranavDarshan/StoryCrafterAI-LangChain-Groq.git
    cd StoryCrafterAI-LangChain-Groq
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up your Groq API key:**
    Create a `.env` file in the project root and add your Groq API key:
    ```
    GROQ_API_KEY=your_groq_api_key
    ```

4.  **Run database migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

The application will be available at `http://127.0.0.1:8000/`.

## Usage

1.  Navigate to the home page.
2.  Enter a text prompt or upload an audio file.
3.  Click "Generate Story".
4.  The application will display the generated story, character and background descriptions, and the combined image.
