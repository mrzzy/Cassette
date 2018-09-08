#
# models.py
# Cassette - Backend
# Interface to acccess the various ML models used in
#

from abc import ABC, abstractmethod

import os.path as path
import math
import numpy as np
import speech_recognition as sr
import wave

# Global flags
VERBOSE = True
    
# Abstract class to represent speech to text model
class TranscribeModel(ABC):

    # Transcribe the given wave audio object into text
    # Returns the transcribed text
    @abstractmethod
    def transcribe(self, audio):
        pass
    
# Represents a external speech to text model 
# using Google's speech to text cloud api
class ExternalModel(TranscribeModel):
    def __init__(self):
        self.recogizer = sr.Recognizer()

    def transcribe(self, audio):
        data = self.convert_data(audio)
        return self.recogizer.recognize_google(data)
    
    # Convert wave object to AudioData object
    def convert_data(self, audio):
        sample_rate = audio.getframerate()
        sample_width = audio.getsampwidth()
        frame_data = audio.readframes(audio.getnframes())
        data = sr.AudioData(frame_data, sample_rate, sample_width)

        return data
    
if __name__ == "__main__":
    model = ExternalModel()
    f = wave.open("/Users/zzy/Downloads/OSR_us_000_0010_8k.wav", "rb")
    print(model.transcribe(f))
