#
# transcribe.py
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

    # Transcribe the given wave file given by path
    # Returns the transcribed text
    @abstractmethod
    def transcribe(self, path):
        pass
    
# Represents a external speech to text model 
# using Google's speech to text cloud api
class ExternalModel(TranscribeModel):
    def __init__(self):
        self.recogizer = sr.Recognizer()

    def transcribe(self, path):
        audio_file = sr.AudioFile(path)
        with audio_file as source:
            audio = self.recogizer.record(source)
            return self.recogizer.recognize_google(audio)
    
    
if __name__ == "__main__":
    model = ExternalModel()
    f = wave.open("/Users/zzy/Downloads/OSR_us_000_0010_8k.wav", "rb")
    print(model.transcribe(f))
