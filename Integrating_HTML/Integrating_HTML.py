#Integrate HTML with Flask
#HTTP verb GET and POST

from flask import Flask,redirect,url_for,render_template,request

app = Flask(__name__)

@app.route('/')
def message():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    var = "PASS"
    return render_template('result.html',result = var)

@app.route('/fail/<int:score>')
def fail(score):
    var = "FAIL"
    return render_template('result.html',result = var)
@app.route('/submit',methods = ['POST','GET'])
def submit():
    total_score = 0
    if(request.method == 'POST'):
        datascience = float(request.form['datascience'])
        ml = float(request.form['ML'])
        ai = float(request.form['AI'])
        total_score = (datascience+ml+ai)/4
    if(total_score>=35):
        return redirect(url_for('success',score = total_score))
    else:
        return redirect(url_for('fail',score = total_score))



if(__name__ == '__main__'):
    app.run(debug = True)


