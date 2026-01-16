from nltk.sentiment.vader import SentimentIntensityAnalyzer
from .schemas import EmotionResult

_analyzer = SentimentIntensityAnalyzer()


def analyze_emotion(text: str) -> EmotionResult:
    scores = _analyzer.polarity_scores(text)
    compound = scores["compound"]

    if compound >= 0.8:
        emotion = "excited"
    elif compound >= 0.6:
        emotion = "happy"
    elif compound <= -0.6:
        emotion = "frustrated"
    elif -0.2 <= compound <= 0.2:
        emotion = "neutral"
    else:
        emotion = "concerned"


    intensity = min(abs(compound), 1.0)

    return EmotionResult(
        emotion=emotion,
        intensity=intensity
    )
