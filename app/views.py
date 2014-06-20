from flask import render_template
from app import app

@app.route('/')
def index():
  #return '<h1>Hello World!</h1>'
  return render_template('index.html')