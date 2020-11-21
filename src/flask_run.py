from flask import Flask, flash, redirect, render_template, request, url_for, g, Response
import connectToDB

app = Flask(__name__)

global parkingOwnerAuthentication

@app.route("/", methods = ['GET', 'POST'])
def home():
    title = "Welcome to verifiedParking"
    return render_template("index.html", title=title ) 



@app.route("/login_parkinglotowner", methods = ['GET', 'POST'])
def login_parkinglotowner():
    if request.method == 'POST':
        if "login" in request.form:
            print("HERE")
            isValid = connectToDB.findOwner('ParkingLotOwners', request.form['username'], request.form['password'])
            if (isValid == True):
                print("VALID")
                return redirect(url_for('parkinglotowner'))
            else:
                print("NOT VALID")
                return redirect(url_for('login_parkinglotowner'))

        elif "register" in request.form:
            return redirect(url_for('registerOwner.html'))

    return render_template("login_parkinglotowner.html" )


@app.route("/parkinglotowner", methods = [ 'GET', 'POST'])
def parkinglotowner():
    
    return render_template("parkinglotowner.html")

@app.route("/register_owner", methods = ['GET', 'POST'])
def register_owner():
    return render_template("registerOwner.html")

@app.route("/user")
def user():

    return render_template("user.html")

if __name__ == "__main__":
    app.run()
