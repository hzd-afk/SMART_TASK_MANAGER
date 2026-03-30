import speech_recognition as sr
from stt.utils import get_microphone

recognizer = sr.Recognizer()

def speech_to_text():
    with get_microphone() as source:

        print("Calibrating noise...")
        recognizer.adjust_for_ambient_noise(source)

        print("Speak now...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("Recognized:", text)
        return text.lower().strip()

    except sr.UnknownValueError:
        print("Could not understand audio")
        return ""

    except sr.RequestError:
        print("API error")
        return ""