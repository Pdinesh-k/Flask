from flask import Flask

app = Flask(__name__)

@app.route('/')
def message():
    return "This is a message okayy"

@app.route('/vanakkam')
def vanakkam():
    return "vanakkam"

if __name__ == '__main__':
    app.run(debug = True)