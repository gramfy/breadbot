from flask import Flask, render_template, request
from threading import Thread
"""
class TheData():
  password=None

class DataUpdate():
  password=None
  islogged=None
  success=False
"""
"""
app = Flask("")
@app.route('/form/')
def form():
  return render_template("index.html")

@app.route('/data/', methods=["POST", "GET"])
def data():
  if request.method == "GET":
    return "The data was tried to be accessed directly. ACCESS DENIED"

  if request.method == "POST":
    form=request.form
    print(form)
    #this is where the data is already sent
    DataUpdate.password = form['passfield']
    if(DataUpdate.password == TheData.password):
        DataUpdate.success=True
        return "Success!"
    else:
        return "Success but the password is probably wrong."
"""

app=Flask("")

@app.route("/")
def home():
    return "In development"

def run():
    app.run(host='0.0.0.0', port=8080)
    
def keep_alive():
    t = Thread(target=run)
    t.start()
