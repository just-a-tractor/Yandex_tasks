from flask import Flask, render_template, redirect, request
import json
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


app = Flask(__name__)

app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        form = LoginForm()
        if form.validate_on_submit():
            return redirect('/success')
        return render_template('index.html', title='Авторизация', form=form)
    elif request.method == 'POST':
        ans = '0'
        login1 = ''
        with open("login.json", "rt", encoding="utf8") as f:
            login_list = json.loads(f.read())
        for i in login_list:
            if request.form['username'] == i['login']:
                ans = '1'
                login1 = i['login']
                if request.form['password'] == i['password']:
                    ans = '2'
        return render_template('answer.html', ans=ans, login1=login1)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
