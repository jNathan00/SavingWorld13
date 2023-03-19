from flask import Flask, render_template, request

app = Flask(__name__)

timetable = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        subject = request.form['subject']
        day = request.form['day']
        time = request.form['time']
        timetable.append({'subject': subject, 'day': day, 'time': time})
    return render_template('index.html', subjects=timetable)

if __name__ == '__main__':
    app.run(host="0.0.0.0")


