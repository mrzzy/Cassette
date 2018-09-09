#
# client.py
# Cassette Models Client
#

from backend.sentinet.client import predict_sentiment
from backend.transcribe import ExternalModel

transcriber = ExternalModel()

# Conduct transcription and sentiment detection on the wav file given by path
# Returns text, feeling_map
def predict(path):
    text = transcriber.transcribe(path)
    feeling_map = predict_sentiment(path)

    return text, feeling_map

if __name__ == "__main__":
    print(predict("/Users/zzy/Desktop/Untitled.wav"))
