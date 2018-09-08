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



# Abstract class to represent speech to text model
class TranscribeModel(ABC):
    @abstractmethod
    
    # Transcribe the given wave audio object into text
    # Returns the transcribed text
    def transcribe(audio):
        pass

# Represents a pretrained Deep Speech model for
# use to convert wave contents to text
class DeepSpeechModel(TranscribeModel):
    WORK_DIR = "dp_model/"
    
    def __init__():
        # Setup working directory
        if not os.path.exists(WORK_DIR): os.mkdir(WORK_DIR)
        os.chdir(WORK_DIR)

        
    # Retrieve the pretrained model and saves it in the pretrained working 
    # directory
    def retrieve_pretrained():
        if VERBOSE: print("retrieveing pretrained model...")
    
if __name__ == "__main__":
    # Unit tests
    retrieve_url("http://www.google.com", "test")
