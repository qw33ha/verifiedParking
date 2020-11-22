from flask import Flask, flash, redirect, render_template, request, url_for, g, Response, session
import connectToDB

app = Flask(__name__)
app.secret_key = "super secret key"


global parkingOwnerAuthentication
parkingOwnerAuthentication = [False]

@app.route("/", methods = ['GET', 'POST'])
def home():
    title = "Welcome to verifiedParking"
    return render_template("index.html", title=title ) 



@app.route("/login_parkinglotowner", methods = ['GET', 'POST'])
def login_parkinglotowner():
    if request.method == 'POST':
        if "login" in request.form:
            isValid = connectToDB.findOwner('ParkingLotOwners', request.form['username'], request.form['password'])
            if (isValid == True):
                print("VALID")
                parkingOwnerAuthentication[0] = True
                session['ownerUsername'] = request.form['username']
                return redirect(url_for('parkinglotowner'))
            else:
                print("NOT VALID")
                #parkingOwnerAuthentication = False
                return render_template("login_parkinglotowner.html", error = "INVALID CREDENTIALS" ) 

        elif "register" in request.form:
            return redirect(url_for('registerOwner.html'))

    return render_template("login_parkinglotowner.html" )


@app.route("/parkinglotowner", methods = [ 'GET', 'POST'])
def parkinglotowner():
    if parkingOwnerAuthentication[0] == True:
        ownerUsername = session.get('ownerUsername', None) 

        if request.method == 'POST':
            if "enters" in request.form:
                connectToDB.modifyOwnerCurrentCapacity('ParkingLotOwners', ownerUsername, 1)
            elif "exits" in request.form:
                connectToDB.modifyOwnerCurrentCapacity('ParkingLotOwners', ownerUsername, -1)
        return render_template("parkinglotowner.html", ownerUsername = ownerUsername)
    else:
        return redirect(url_for('login_parkinglotowner')) 

@app.route("/register_owner", methods = ['GET', 'POST'])
def register_owner():
    return render_template("registerOwner.html")

@app.route("/user")
def user():

    return render_template("user.html")

if __name__ == "__main__":
    app.run()
