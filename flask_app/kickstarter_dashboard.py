from flask import Flask, request, render_template, url_for, redirect
from predict import categoryList, kickstarter_prediction

app = Flask(__name__)

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/categories')
def categories():
    return render_template('categoryList.html', categoryList=categoryList)

@app.route('/data/', methods=['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"Wrong URL"
    if request.method == 'POST':
        form_data = request.form
        return render_template('data.html', form_data=form_data)

@app.route('/')
def landing():
    return redirect(url_for('form'))

app.run()