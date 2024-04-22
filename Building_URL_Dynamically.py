#Building URL Dynamically
#Variable Rules and URL Dynamically


from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route('/')
def message():
    return 'Welcome welcome welcome'

@app.route('/success/<int:score>')
def success(score):
    return 'Person passed the exam and the marks is '+str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return 'Person failed the exam and the marks is '+str(score)

@app.route('/results/<int:marks>')
def results(marks):
    container = ''
    if(marks<35):
        container = 'fail'
    else:
        container = 'success'
    return redirect(url_for(container,score=marks))


if __name__ == '__main__':
    app.run(debug = True)