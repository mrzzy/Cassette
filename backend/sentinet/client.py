#
# src/client.py
# Sentinet Model Client
#

from keras import models
from backend.sentinet.dataset import extract_feature, LABEL_MAP

import numpy as np

# Predict the sentiment of the wav file given by path 
# Returns dict of predicted name of feeling to intensity 
model = models.load_model("backend/sentinet/model.h5")
def predict_sentiment(path):
    # Extract features
    features = extract_feature(path)
    features = np.reshape(features, (1,) + features.shape)

    # Predict sentiment
    predictions = model.predict(features)[0]

    # Compute max label 
    max_i = 0
    max_pred = 0
    for i in range(len(predictions)):
        if predictions[i] > max_pred:
            max_pred = predictions[i]
            max_i = i
    
    
    names = [ l[0] for l in LABEL_MAP ]
    return names[max_i]

if __name__ == "__main__":
    print(predict_sentiment("/Users/zzy/Desktop/Untitled.wav"))

