from flask import Flask, request, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, RadioField
from wtforms.validators import DataRequired
import json
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


class OprosForm(FlaskForm):
    name = StringField('Ваше имя', validators=[DataRequired()])
    loyal = BooleanField('Удовлетворены ли вы своей зарплатой?', validators=[DataRequired()])
    zarab = RadioField('Ваша зарплата', choices=[('small', 'меньше 100.000 руб./месяц'),
                                                 ('norm', 'больше 100.000 руб./месяц'),
                                                 ('big', 'значительно больше 100.000 руб./месяц')])


@app.route('/', methods=['GET', 'POST'])
@app.route('/little_survey', methods=['GET', 'POST'])
def image_sample():
    form = OprosForm()
    if request.method == 'GET':
        return render_template('opros.htm', form=form)
    elif request.method == 'POST':
        data = dict(request.form)
        name = data['name'][0]
        with open('{}.json'.format(name + ' ' + datetime.datetime.today().strftime("%Y-%m-%d")), 'w') as outfile:
            data.pop('csrf_token')
            json.dump(data, outfile, ensure_ascii=False)
        return render_template('end_page.htm', form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
