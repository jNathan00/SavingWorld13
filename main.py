from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Route to display the timetable
@app.route('/timetable', methods=['GET'])
def timetable():
    conn = sqlite3.connect('timetable.db')
    c = conn.cursor()
    c.execute("SELECT * FROM events")
    events = c.fetchall()
    conn.close()
    return render_template('timetable.html', events=events)

# Route to add an event to the timetable
@app.route('/add_event', methods=['POST'])
def add_event():
    name = request.form['name']
    start_time = request.form['start_time']
    end_time = request.form['end_time']
    date = request.form['date']
    conn = sqlite3.connect('timetable.db')
    c = conn.cursor()
    c.execute("INSERT INTO events (name, start_time, end_time, date) VALUES (?, ?, ?, ?)", (name, start_time, end_time, date))
    conn.commit()
    conn.close()
    return 'Event added successfully!'

if __name__ == '__main__':
    app.run(debug=True)

