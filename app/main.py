from fastapi import FastAPI
from app.core.sentiment import analyze_emotion
from app.core.voice_engine import build_voice_config, synthesize_speech
from app.core.schemas import TextInput
from fastapi.responses import FileResponse
from fastapi.responses import HTMLResponse
import os


app = FastAPI(title="The Empathy Engine")

OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)


@app.post("/synthesize")
def synthesize(input: TextInput):
    # 1. Analyze emotion
    emotion_result = analyze_emotion(input.text)

    # 2. Build voice configuration
    voice_config = build_voice_config(
        emotion_result.emotion,
        emotion_result.intensity
    )

    # 3. Generate audio
    output_path = os.path.join(OUTPUT_DIR, "output.wav")
    synthesize_speech(input.text, voice_config, output_path)

    return {
        "emotion": emotion_result.emotion,
        "intensity": emotion_result.intensity,
        "audio_file": output_path,
        "playback_url": "http://127.0.0.1:8000/play"
    }


@app.get("/audio")
def get_audio():
    return FileResponse(
        path="output/output.wav",
        media_type="audio/wav",
        filename="output.wav"
    )



@app.get("/play", response_class=HTMLResponse)
def play_audio():
    return """
    <html>
      <body>
        <h3>Empathy Engine Output</h3>
        <audio controls autoplay>
          <source src="/audio" type="audio/wav">
          Your browser does not support audio.
        </audio>
      </body>
    </html>
    """
