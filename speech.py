import speech_recognition as sr
from gtts import gTTS
from tempfile import NamedTemporaryFile
from playsound import playsound


def speech_to_text():
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
        return r.recognize_google(audio)


def text_to_speech(text):
    gTTS(text).write_to_fp(voice := NamedTemporaryFile())
    playsound(voice.name)
    voice.close()
