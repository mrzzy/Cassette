from flask import Flask, request, render_template, redirect, jsonify
import datetime


app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')


# requests
@app.route('/audioprocess', methods=['POST'])
def audioprocess():
    if request.method == 'POST':
        # do something if its post

        audio_bytes = request.data

        # write the bytes out in wav
        filedate = str(datetime.datetime.now())
        string_wav = filedate + '.wav'
        print(string_wav)
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

        # return 'post request reached here'
        return_text = ('i am an angry flower', {'angry': 0.5})
        print(return_text[0])
        return jsonify(
            text=return_text[0],
            emotion=return_text[1]
        )
    else:
        # not a post request but they got here anyways
        return redirect('/')


if __name__ == '__main__':
    app.run(debug=True, port=8234, ssl_context='adhoc')
