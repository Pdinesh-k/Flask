from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def message():
    return render_template('Calculator_index.html')

@app.route('/submit',methods = ["POST","GET"])
def calculate():

    if(request.method=="POST"):
        add_in = request.form['add']
        sub_in = request.form['sub']
        mul_in = request.form['mul']
        div_in = request.form['div']

        add = [int(i) for i in add_in.split(',')]
        sub = [int(i) for i in sub_in.split(',')]
        mul = [int(i) for i in mul_in.split(',')]
        div = [int(i) for i in div_in.split(',')]

        add = add[0]+add[1]
        sub = sub[0]-sub[1]
        mul = mul[0]*mul[1]
        div = div[0]/div[1]

        return render_template('result.html',add = add , sub = sub,
                               mul = mul , div = div)





if(__name__ == '__main__'):
    app.run(debug = True)