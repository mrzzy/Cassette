from flask import Flask, request, render_template, redirect


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
        f = open('audio.wav', 'wb')
        f.write(audio_bytes)
        f.close()

        # write some functions here and return it back

        return 'post request reached here'
    else:
        # not a post request but they got here anyways
        return redirect('/')


if __name__ == '__main__':
    app.run(debug=True, port=8234, ssl_context='adhoc')
