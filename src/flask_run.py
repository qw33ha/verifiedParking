from flask import Flask, redirect, url_for, render_template, jsonify
import json

app = Flask(__name__)


@app.route("/")
def home():
    title = "Welcome to verifiedParking"
    return render_template("index.html", title=title ) 

if __name__ == "__main__":
    app.run()
