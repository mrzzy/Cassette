#
# models.py
# Cassette - Backend
# Interface to acccess the various ML models used in
#

from abc import ABC, abstractmethod
from deepspeech.client import Model

import os.path as path
import requests
import tarfile
import math
import librosa
import numpy as np

# Global flags
VERBOSE = True

# Utility functions
# Downloads a file from given src_url and saves it in dest_path
# Supports large files by downloading in chunks
def retrieve_url(src_url, dest_path, chunk_len=16*1024):
    r = requests.get(src_url, stream=True)
    if r.status_code != 200:
        raise ValueError("Failed to open resource at {}".format(src_url))
    
    # Compute number of chunks to retrieve based on resource size
    resource_len = int(r.headers["content-length"])
    n_chunk = math.ceil(resource_len / chunk_len)

    # Retrieve in chunks to reduce memory usage
    if VERBOSE: print("Retriving: ", src_url)
    f = open(dest_path, "wb")
    n_recieved = 0
    for chunk in r.iter_content(chunk_size=chunk_len): 
        if chunk: # Filter out keep alive chunks
            # Display retireval status
            n_recieved += 1
            if VERBOSE:
                percentage = n_recieved / n_chunk * 100.0
                print("{:.1f}%".format(percentage))

            # Write chunk to disk
            f.write(chunk)
            f.flush()
            
    f.close()

# Extract the tarball at the filepath path in the current directory
def extract_tarball(path):
    tar = tarfile.open(path, "r:gz")
    tar.extractall()
    tar.close()
    
# Read the wav file given path as a float numpy array
# Forces the audio into a mono (single) audio channel
# Returns the audio as a numpy array
def read_wav(path, sample_rate=16000):
    audio, sample_rate = librosa.core.load(path, sr=sample_rate)
    return audio

# Encode the given numpy array to an integer array of the given bits
def encode_integer(array, n_bits):
    max_val = 2 ** n_bits - 1
    dtype = "int{}".format(n_bits)
    return (array * max_val).astype(dtype)

# Abstract class to represent speech to text model
class TranscribeModel(ABC):
    # Transcribe the given wave audio object into text
    # Returns the transcribed text
    @abstractmethod
    def transcribe(self, audio):
        pass

# Represents a pretrained Deep Speech model for
# use to convert wave contents to text
class DeepSpeechModel(TranscribeModel):
    WORK_DIR = "work_deepspeech"
    MODEL_PATH = path.join(WORK_DIR, "models")

    # Constants copied from :
    # https://github.com/mozilla/DeepSpeech/blob/master/native_client/python/client.py
    BEAM_WIDTH = 500
    LM_WEIGHT = 1.75
    VALID_WORD_COUNT_WEIGHT = 1.00
    N_FEATURES = 26
    N_CONTEXT = 9
    
    def __init__(self):
        # Setup working directory
        if not path.exists(DeepSpeechModel.WORK_DIR): 
            mkdir(DeepSpeechModel.WORK_DIR)
        # Retrieve pretrained model if does not already exist
        if not path.exists(DeepSpeechModel.MODEL_PATH): self.retrieve()
        
    # Retrieve the pretrained model and saves it in the pretrained working 
    # directory
    def retrieve(self):
        if VERBOSE: print("Retrieving pretrained model...")
        
        # Retrive model
        model_url = "https://github.com/mozilla/DeepSpeech/releases/download/v0.1.1/deepspeech-0.1.1-models.tar.gz"
        compressed_model_path = path.join(DeepSpeechModel.WORK_DIR, 
                                             path.basename(model_url))
        retrieve_url(model_url, compressed_model_path)
        
        # Extract model
        extract_tarball(compressed_model_path)
        assert path.exists(DeepSpeechModel.MODEL_PATH)
        

    

if __name__ == "__main__":
    pass
