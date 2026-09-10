from flask import flask 
app = flask(_name_)
@app.route("/")
def home():
     return "hello from docker! my first container is runnimg."
  if_name_=="_manin_":
    app.run(host="0.0.0.0",port=5000)
