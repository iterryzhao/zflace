from flask import render_template,request
from app import app
from forms import ContactForm
from flask.ext.mail import Mail,Message

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/contact/', methods=['GET','POST'])
def contact():
  name = None
  phone = None
  msg = None
  email = None
  form = ContactForm()
  print 'asdfasdfasd'
  #if form.validate_on_submit():
  if request.method=='POST':
    name = request.form['name']
    phone = request.form['phone']
    email = request.form['email']
    msg = request.form['message']
    print msg
    #owner_email = request.form['owner_email']
    mail = Mail(app)
    print 'testing'
    message = Message("From"+name, sender="16715906@qq.com", recipients=["16715906@qq.com"])
    #message.body="testing terry"
    message.html=msg+"<br/>Contact me via email: "+email
    mail.send(message)
  print "success"
  return render_template('contact.html'
    , form=form)


@app.route('/product/')
def product():
  return render_template('product.html')

@app.route('/product/<name>')
def product_id(name):
  return render_template('product.html', name = name)
'''
@app.errorhandler(404)
def page_not_found(e):
  return render_template('404.html'),404

@app.errorhandler(500)
def internal_server_error(e):
  return render_template('500.html'),500
'''
