from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/c')
def character():
    return render_template('character.html')

if __name__ == "__main__":
    app.run(debug=True)