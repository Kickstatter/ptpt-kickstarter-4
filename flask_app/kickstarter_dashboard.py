from flask import Flask, request, render_template
from flask_app.predict import kickstarter_prediction

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')


@app.route('/data/', methods=['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"Wrong URL"
    if request.method == 'POST':
        form_data = request.form
        return render_template('data.html', form_data=form_data)


app.run()