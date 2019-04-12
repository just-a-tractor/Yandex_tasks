from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
@app.route('/div_mod', methods=['GET', 'POST'])
def div_mod():
    if request.method == 'GET':
        return render_template('index2.html', number1=8, number2=2)
    elif request.method == 'POST':
        try:
            num1 = int(request.form['number1'])
            num2 = int(request.form['number2'])
        except ValueError:
            num1 = 0
            num2 = 0
        return render_template('index2.html', number1=num1, number2=num2)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
