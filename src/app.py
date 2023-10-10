from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/trabalhos')
def trabalhos():
    return render_template('trabalhos.html')

if __name__ == "__main__":
    app.run(debug=True)
