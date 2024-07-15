from flask import Flask, request, jsonify, render_template, url_for, redirect
#from werkzeug.utils import secure_filename

app = Flask(__name__)
@app.route('/')
def home_page():
    return render_template("index.html")

@app.route('/about')
def about_page():
    return render_template("history.html")

@app.route('/aboutPESU')
def about_PESU_page():
    return render_template("about.html")

@app.route('/events')
def about_events_page():
    return render_template("events.html")

if __name__ == '__main__':
    app.run(debug=True)