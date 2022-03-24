from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  
app.secret_key = "Let's Buy Fruit!"
@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    total = int(request.form['apple']) + int(request.form['raspberry']) + int(request.form['strawberry'])
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['student_id'] = request.form['student_id']
    session['student_id'] = request.form['student_id']
    session['apple'] = request.form['apple']
    session['strawberry'] = request.form['strawberry']
    session['raspberry'] = request.form['raspberry']
    session['total'] = total
    print("Charging", session['first_name'], session['last_name'], "for", session['total'], "fruits")
    return redirect("/checking-out")

@app.route('/checking-out')
def checkingOut():
    return render_template("checkout.html")

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    