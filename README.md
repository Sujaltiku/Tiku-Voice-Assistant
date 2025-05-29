# Tiku-Voice-Assistant
# 🎙️ Tiku Assistant

**Tiku** is a voice-activated AI desktop assistant built with Python. It can listen to your voice, respond intelligently, search Google, play music from YouTube, open apps, and answer factual questions using WolframAlpha.
		Sign up for WolframAlpha API:
Go to WolframAlpha Developer Portal and create a free account to get your App ID.
      Create a .env file in the project root and add your WolframAlpha App ID:
---

## ✨ Features

- 🔊 Wake word: Say **"Tiku"** to activate hands-free mode
- 🗣️ Voice command recognition
- 📺 Play YouTube music using keywords
- 🌐 Google search for anything
- 🧠 Ask questions with WolframAlpha
- 🧠 Optional ChatGPT (OpenAI) integration
---

## 🛠️ Tech Stack

- Python 3.x
- `speech_recognition`
- `pyttsx3` (text-to-speech)
- `pywhatkit` (YouTube playback)
- `wolframalpha`
- `openai` (optional, for GPT responses)
- `python-dotenv` (to manage API keys)

---

## 🖥️ How to Run

1. **Clone the repo**:
   ```bash
   git clone https://github.com/yourusername/tiku-assistant.git
   cd tiku-assistant
