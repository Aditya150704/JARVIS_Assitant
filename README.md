# JARVIS_Assitant
🧠 Jarvis - Voice Assistant (Python)
Jarvis is a Python-based voice assistant that listens for voice commands, speaks responses using text-to-speech, and can interact with web browsers, play music, fetch news, and answer general queries using OpenAI's ChatGPT.

🔧 Features
🗣️ Voice Activation: Say "Jarvis" to activate the assistant.

🌐 Web Navigation: Opens Google, YouTube, Facebook, or LinkedIn on command.

🎶 Music Playback: Plays songs from a custom library.

📰 News Headlines: Fetches top news from India via NewsAPI.

💬 AI Responses: Uses OpenAI's GPT-3.5 for general-purpose Q&A.

🔊 Speech Output: Speaks responses using Google Text-to-Speech (gTTS) and Pygame.

📦 Requirements
Python 3.10+

Dependencies:

bash
Copy
Edit
pip install SpeechRecognition pyttsx3 pygame gtts requests openai
📁 Project Structure
main.py - Main logic of the assistant.

musicLibrary.py - A Python file containing a dictionary of song names and their URLs (must be created).

🚀 Getting Started
Clone the repository.

Add your API key for OpenAI and NewsAPI in main.py.

Create a musicLibrary.py file with a dictionary named music.

Run the assistant:

bash
Copy
Edit
python main.py
⚠️ Notes
Internet connection is required for speech recognition, OpenAI API, gTTS, and NewsAPI.

Make sure your microphone is working.

The program uses a hardcoded OpenAI key — replace it with your own for security.

