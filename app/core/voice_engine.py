import pyttsx3
from .schemas import VoiceConfig

_engine = pyttsx3.init()

BASE_RATE = 170
BASE_VOLUME = 1.0


def build_voice_config(emotion: str, intensity: float) -> VoiceConfig:
    rate = BASE_RATE
    volume = BASE_VOLUME

    if emotion == "happy":
        rate += int(40 * intensity)
        volume = min(1.0, volume + 0.2 * intensity)

    elif emotion == "frustrated":
        rate -= int(30 * intensity)
        volume = max(0.6, volume - 0.2 * intensity)

    return VoiceConfig(rate=rate, volume=volume)


def synthesize_speech(text: str, config: VoiceConfig, output_path: str):
    _engine.setProperty("rate", config.rate)
    _engine.setProperty("volume", config.volume)

    _engine.save_to_file(text, output_path)
    _engine.runAndWait()
