import speech_recognition as sr

def listen(level=""):
    audio = None
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(level+"listening")
        audio = r.listen(source, phrase_time_limit=3)
        print(level+"thinking...")
    return audio

def lsiten_silently():
    audio = None
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source, phrase_time_limit=3)
    return audio
