from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/aboutme')
def aboutme():
    return render_template('aboutme.html')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
