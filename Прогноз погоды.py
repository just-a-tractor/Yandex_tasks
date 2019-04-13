from flask import Flask, render_template, request
import json


def pod(wl):
    a = []
    str_pod = [i for i in list(wl[list(wl.keys())[0]]['podrobn'].keys())]

    for i in str_pod:
        a.append(i + ': ' + wl[list(wl.keys())[0]]['podrobn'][i])

    return a


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
@app.route('/weather', methods=['GET', 'POST'])
def weather():

    with open("weather.json", "rt", encoding="utf8") as f:
        weather_list = json.loads(f.read())

    if request.method == 'GET':
        return render_template('first-page.html')
    elif request.method == 'POST':
        time = request.form['time']
        if time == 'day':
            str_pod = pod(weather_list)
            return render_template('{}.html'.format(time), date=list(weather_list.keys())[0],
                                   tem=weather_list[list(weather_list.keys())[0]]['temp'],
                                   pod=str_pod)
        elif time == 'three_days':
            a = []
            for i in range(3):
                a.append(list(weather_list.keys())[i])
                a.append(weather_list[list(weather_list.keys())[i]]['temp'])
                a.append(weather_list[list(weather_list.keys())[i]]['kratk'])
                a.append(' ')
            return render_template('{}.html'.format(time), krs=a)

        elif time == 'week':
            a = []
            for i in range(7):
                a.append(list(weather_list.keys())[i])
                a.append(weather_list[list(weather_list.keys())[i]]['temp'])
                a.append(weather_list[list(weather_list.keys())[i]]['kratk'])
                a.append(' ')
            return render_template('{}.html'.format(time), krs=a)

        elif time == 'month':
            a = []

            for i in range(31):
                a.append((list(weather_list.keys())[i], weather_list[list(weather_list.keys())[i]]['temp']))

            return render_template('{}.html'.format(time), tab=a)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
