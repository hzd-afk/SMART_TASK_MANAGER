import speech_recognition as sr

def get_microphone():
    return sr.Microphone()

def list_microphones():
    mics = sr.Microphone.list_microphone_names()
    for i, name in enumerate(mics):
        print(f"[{i}] {name}")