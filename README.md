# The Empathy Engine 🎙️

The Empathy Engine is an AI-powered Text-to-Speech (TTS) service that generates emotionally expressive speech from text.  
Unlike traditional robotic TTS systems, this service detects the **emotion and intensity** of the input text and dynamically modulates vocal characteristics to produce more human-like audio output.

---

## 🚀 Features

- Emotion detection from text using sentiment analysis
- Supported emotions:
  - Excited
  - Happy
  - Neutral
  - Concerned
  - Frustrated
- Emotion intensity scaling
- Dynamic voice modulation:
  - Speech rate
  - Pitch
  - Volume
- Generates playable `.wav` audio output
- REST API built using FastAPI
- Interactive API documentation via Swagger UI

---

## 🛠️ Tech Stack

- **Python**
- **FastAPI** – API framework
- **NLTK (VADER)** – sentiment & emotion detection
- **pyttsx3** – offline Text-to-Speech engine
- **Uvicorn** – ASGI server

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/thej-alt/empathy-engine.git
cd empathy-engine
```
### 2️⃣ Create and activate virtual environment
```bash
python -m venv venv
```
### Windows:
```bash
venv\Scripts\activate
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
### 4️⃣ Run the application
```bash
uvicorn app.main:app --reload
```
### 5️⃣ Open Swagger UI

Open your browser and go to:
```bash
http://127.0.0.1:8000/docs
```

---

## 📡 API Usage
POST /synthesize

### Request Body :
```json
{
  "text": "Nothing is working and this is really irritating."
}
```

### Response :
```json
{
  "emotion": "concerned",
  "intensity": 0.5095,
  "audio_file": "output\\output.wav",
  "playback_url": "http://127.0.0.1:8000/play"
}
```
The generated audio file can be played locally from the output directory.
---

## 🧠 Design Choices & Emotion Mapping

Emotion Detection

VADER sentiment analysis was chosen for its speed, simplicity, and interpretability.

The compound sentiment score is used to classify emotions:
| Compound Score Range | Emotion    |
| -------------------- | ---------- |
| ≥ 0.8                | Excited    |
| 0.6 – 0.79           | Happy      |
| -0.2 – 0.2           | Neutral    |
| -0.59 – -0.21        | Concerned  |
| ≤ -0.6               | Frustrated |

This separation allows the system to distinguish between strong excitement, general positivity, and mild concern, which is crucial for realistic voice modulation.

Intensity Scaling :

Emotion intensity is calculated as the absolute value of the compound sentiment score.

This intensity value controls how strongly voice parameters are modulated.

Voice Modulation Logic :

Each detected emotion maps to a predefined voice configuration :

Excited :

    Faster speech rate

    Higher pitch

    Increased volume

Happy :

    Slightly faster rate

    Moderately higher pitch

    Normal volume

Neutral :

    Default rate

    Default pitch

    Default volume

Concerned :

    Slightly slower rate

    Lower pitch

    Softer volume

Frustrated :

    Slower speech rate

    Lower pitch

    Reduced volume

This deterministic mapping ensures the system remains explainable, reproducible, and easy to extend.

--- 
## 🔮 Future Improvements:
    -> SSML-based fine-grained voice control

    -> Real-time audio streaming in API response

    -> Transformer-based emotion classification

    -> Frontend UI with embedded audio playback.
---

## 🧩 API Design Notes :
The service is implemented as a REST API to allow easy integration with web, mobile, or backend systems. 
FastAPI was chosen for its automatic documentation, validation, and production readiness.

---
## 📁 Project Structure :
app/
 ├── main.py            # FastAPI entry point
 ├── core/
 │   ├── sentiment.py   # Emotion detection logic
 │   ├── voice_engine.py# Voice modulation & TTS
 │   └── schemas.py     # Pydantic models
---
## ⚠️ Limitations :
- Emotion detection is rule-based and may misclassify ambiguous text
- Audio playback is file-based, not streamed

---

## 👤 Author

Krishna Teja Regintala.

ECE Undergraduate | Machine Learning & NLP Enthusiast | DSA Practitioner

---