#
# models.py
# Cassette - Backend
# Interface to acccess the various ML models used in
#

from abc import ABC, abstractmethod

import os
import requests
import tarfile
import math

# Global flags
VERBOSE = True

# Utility functions
# Downloads a file from given src_url and saves it in dest_path
# Supports large files by downloading in chunks
def retrieve_url(src_url, dest_path, chunk_len=1024):
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
                print("{:.2f}%".format(percentage))

            # Write chunk to disk
            f.write(chunk)
            f.flush()
            
    f.close()

# Extract the tarball at the filepath path in the current directory
def extract_tarball(path):
    tar = tarfile.open(path, "r:gz")
    tar.extractall()
    tar.close()

    

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
    WORK_DIR = "dp_model"
    MODEL_PATH = os.path.join(WORK_DIR, "model")
    
    def __init__(self):
        # Setup working directory
        if not os.path.exists(DeepSpeechModel.WORK_DIR): 
            os.mkdir(DeepSpeechModel.WORK_DIR)
        # Retrieve pretrained model if does not already exist
        if not os.path.exists(DeepSpeechModel.MODEL_PATH): self.retrieve_pretrained()
        
    # Retrieve the pretrained model and saves it in the pretrained working 
    # directory
    def retrieve_pretrained(self):
        if VERBOSE: print("Retrieving pretrained model...")
        
        # Retrive model
        model_url = "https://github.com/mozilla/DeepSpeech/releases/downloadv0.1.1/deepspeech-0.1.1-models.tar.gz"
        compressed_model_path = os.path.join(DeepSpeechModel.WORK_DIR, 
                                             os.path.basename(model_url))
        retrieve_url(model_url, compressed_model_path)
        
        # Extract model
        extract_tarball(compressed_model_path)
        assert os.path.exists(DeepSpeechModel.MODEL_PATH)
    
    def transcribe(self, audio):
        pass

if __name__ == "__main__":
    model = DeepSpeechModel()

