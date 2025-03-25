# future_ai
its all about the image and text generation using langchain and streamlit 

# Future AI GPT

## Overview
Future AI GPT is a Streamlit-based web application that integrates **Google Gemini (via LangChain)** and **Stability AI's SD3 model** for text and image generation. Users can enter a prompt to generate AI responses or AI-generated images.

## Features
- **Text Generation:** Uses Google Gemini 1.5 Pro via LangChain.
- **Image Generation:** Uses Stability AI's SD3 model.
- **User Authentication:** Only registered users can access the app.
- **Download Generated Images:** Users can download AI-generated images.
- **Copy AI-Generated Text:** Users can copy or download the generated text.

## Installation
### 1. Clone the Repository
```sh
git clone https://github.com/your-repo/future-ai-gpt.git
cd future-ai-gpt
```

### 2. Install Dependencies
```sh
pip install -r requirements.txt
```

### 3. Run the Application
```sh
streamlit run your_script.py
```

## Configuration
Set up your API keys securely in **Streamlit secrets**:
1. Create a `.streamlit/secrets.toml` file.
2. Add the following:
```toml
[authentication]
user1 = "****"
password1 = ""****""
user2 = ""****""
password2 = ""****""

[STABILITY_API_KEY]
YOUR_STABILITY_API_KEY_HERE

[GEMINI_API_KEY]
YOUR_GEMINI_API_KEY_HERE
```

## Usage
1. **Login** using a registered username and password.
2. **Enter a text prompt** for AI-generated content or images.
3. **Download images** after generation.
4. **Copy AI-generated text** using the copy button.

## License
This project is open-source under the MIT License.

