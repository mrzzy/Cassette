from flask import Flask, request, render_template, redirect, jsonify
import datetime
import os


from backend.client import predict
from backend.sentinet.client import graph

app = Flask(__name__)


emotionMap = {
    'neutral': '#000000',
    'calm': '#212F3C',
    'happy': '#F1C40F',
    'sad': '#515A5A',
    'angry': '#CB4335',
    'fearful': '#9B59B6',
    'disgust': '#5B2C6F',
    'surprised': '#026655'
}


@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')


# requests
@app.route('/audioprocess', methods=['POST'])
def audioprocess():
    if request.method == 'POST':
        # do something if its post
        os.system("rm -r ~/openhse/Cassette/*.wav")
        audio_bytes = request.data

        # write the bytes out in wav
        filedate = str(datetime.datetime.now())
        string_wav = filedate + '.wav'
        f = open(string_wav, 'wb')
        f.write(audio_bytes)
        f.close()

        # write some functions here and return it back

        '''
        return data
        feeling - match against list of feelings with colours
        intensity - 0 to 1
        (text, {feeling: intensity})
        '''

        # return_text = ('i am an angry flower', {'angry': 0.5})
        with graph.as_default():
            return_text = predict(string_wav)
        print(return_text[1])
        return jsonify(
            text=return_text[0],
            color=emotionMap[return_text[1]]
        )
    else:
        # not a post request but they got here anyways
        return redirect('/')


if __name__ == '__main__':
    app.run(debug=True, port=8234, ssl_context='adhoc', host="0.0.0.0")
