from flask import *
import flask

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.errorhandler(404)
def tripped(e):
    return render_template('404.html')

# @app.route('/border')
def rock():
    return render_template('rocky.html')

# @app.route('/border/about-me')
def aboutme():
    return render_template('aboutme.html')

if __name__ == '__main__':
    app.run(debug=True)