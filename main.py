from flask import Flask, render_template, request

app = Flask(__name__, static_url_path='/static')

timetable = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        subject = request.form['subject']
        day = request.form['day']
        timestart = request.form['time start']
        timeend = request.form['time end']
        timetable.append({'subject': subject, 'day': day, 'time start': timestart, 'time end': timeend})
    return render_template('index.html', subjects=timetable)


if __name__ == '__main__':
    app.run(host="0.0.0.0")

