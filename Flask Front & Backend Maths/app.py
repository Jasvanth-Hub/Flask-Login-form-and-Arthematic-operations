from flask import Flask,render_template,request

app = Flask(__name__)


@app.route('/',methods=["GET"])
def welcome():
    return render_template("welcome.html")

@app.route("/Login",methods=["GET"])
def login():
    return render_template("Login.html")

@app.route("/login-form",methods=["POST"])
def login_form():
    fname = request.form['fname']
    lname = request.form['lname']
    email = request.form['email']
    age = request.form['age']
    phone = request.form['phone']

    return {"Details":{"Name":{"First name":fname,"Last name":lname},"Email":email,"age":age,"Phone no":phone}}

@app.route("/add",methods=['GET'])
def addition():
    return render_template("add.html")


@app.route("/addition-form",methods=['POST'])
def addition_form():
    a = request.form['a']
    b = request.form['b']
    return {"Message":f"The addition of {a} and {b} is {int(a)+int(b)}."}


@app.route("/sub",methods=['GET'])
def subtraction():
    return render_template("sub.html")


@app.route("/subtraction-form",methods=['POST'])
def subtraction_form():
    a = request.form['a']
    b = request.form['b']
    return {"Message":f"The subtraction of {a} and {b} is {int(a)-int(b)}."}


@app.route("/mul",methods=['GET'])
def multiplication():
    return render_template("mul.html")

@app.route("/multiplication-form",methods=['POST'])
def multiplication_form():
    a = request.form['a']
    b = request.form['b']
    return {"Message":f"The multiplication of {a} and {b} is {int(a)*int(b)}."}


@app.route("/div",methods=['GET'])
def division():
    return render_template("div.html")


@app.route("/division-form",methods=['POST'])
def division_form():
    a = request.form['a']
    b = request.form['b']
    return {"Message":f"The division of {a} and {b} is {int(a)/int(b)}."}



