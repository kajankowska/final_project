from flask import Flask, render_template

with open("key.txt") as file:
    key = file.readlines()[0]

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
