import speech_recognition as sr
from os import path

class to_text():
    def __init__(self, name="english.wav",  audiofile="E:\\parisa\\projects\\voice_recognition\\voice-recognition-master\\wave_files\\english.wav", yousaid="error"):
        self.name = name
        self.audiofile = audiofile
        self.yousaid = yousaid
    def read_audio(self):
        self.audiofile = path.join(path.dirname(path.realpath("E:\parisa\projects\\voice_recognition\\voice-recognition-master\\wave_files")), "english.wav")
    def print_text(self):
        r = sr.Recognizer()
        with sr.AudioFile(self.audiofile) as source:
            audio = r.record(source)
        self.yousaid = "You said: \n" + r.recognize_google(audio)
    def out_put(self):
        return self.yousaid
