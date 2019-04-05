# import used modules
import speech_recognition as sr
from os import path


class to_text():
    def __init__(self, name="english.wav",  audiofile="E:\\parisa\\projects\\voice_recognition\\voice-recognition-master\\wave_files\\english.wav", yousaid="error"):
        self.name = name
        self.audiofile = audiofile
        self.yousaid = yousaid
    def read_audio(self):
        '''reads path of audio file'''
        self.audiofile = path.join(path.dirname(path.realpath("E:\parisa\projects\\voice_recognition\\voice-recognition-master\\wave_files")), "english.wav")
    def print_text(self):
        r = sr.Recognizer()
        with sr.AudioFile(self.audiofile) as source:    # uses the audio file as the audio source
            audio = r.record(source)    # read the entire audio file
        # print the text of the audio
        self.yousaid = "You said: \n" + r.recognize_google(audio)
    def out_put(self):
        return self.yousaid
