import requests
from flask import Flask, render_template, request 
import psycopg2

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('login.html') 

if __name__ == "__main__":
    app.run(debug=True ,port=8080,use_reloader=False) 