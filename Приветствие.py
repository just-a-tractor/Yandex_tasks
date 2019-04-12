from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
@app.route('/greeting_form', methods=['GET', 'POST'])
def greeting_form():
    if request.method == 'GET':
        return render_template('index.html', name='Васян')
    elif request.method == 'POST':
        name = request.form['name']
        return render_template('index.html', name=name)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
