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

        # data = request.form['data']
        # ml_placeholder is the function that returns text
        # return ml_placeholder(data)
        pass
    else:
        # not a post request but they got here anyways
        return redirect('/')


if __name__ == '__main__':
    app.run(debug=True, port=8234)
