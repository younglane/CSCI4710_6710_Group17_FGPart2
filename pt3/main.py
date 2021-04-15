from flask import Flask, render_template
import os
app = Flask(__name__)



@app.route("/")
def home():
 
    return render_template("home.html")
    
@app.route("/about")
def about():
   
    return render_template("about.html", )

@app.route("/shows")
def shows():
  
    return render_template("shows.html")

    
if __name__ == "__main__":
    app.run()
    ip = '127.0.0.1'
    app.run(host=ip)