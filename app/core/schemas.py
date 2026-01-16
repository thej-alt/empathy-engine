from pydantic import BaseModel
from typing import Literal


class TextInput(BaseModel):
    text: str


class EmotionResult(BaseModel):
    emotion: Literal[
    "happy",
    "neutral",
    "frustrated",
    "concerned",
    "excited"
    ]

    intensity: float


class VoiceConfig(BaseModel):
    rate: int
    volume: float
