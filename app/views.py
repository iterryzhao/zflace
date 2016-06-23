from flask import render_template,request
from app import app
from forms import ContactForm
from flask_mail import Mail,Message

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/contact/', methods=['GET','POST'])
def contact():
  name = None
  #phone = None
  msg = None
  email = None
  form = ContactForm()
  #if form.validate_on_submit():
  if request.method=='POST':
    name = request.form['name']
    #phone = request.form['phone']
    email = request.form['email']
    msg = request.form['message']
    #owner_email = request.form['owner_email']
    mail = Mail(app)
    message = Message("From"+name+" via ZFLACE.COM", sender="16715906@qq.com", recipients=["16715906@qq.com"])
    #message.body="testing terry"
    message.html=msg+"<br/>Contact me via email: "+email
    mail.send(message)
  return render_template('contact.html'
    , form=form)


@app.route('/product')
def product():
  return render_template('product.html')
  
@app.route('/product/<name>')
def product_id(name):
  if name=='small_lace':
    return render_template('small_lace.html')
  elif name=='lace_fabric':
    return render_template('lace_fabric.html')
  elif name=='jacquard_lace':
    return render_template('jacquard_lace.html')
  elif name=='embroidery_fabric':
    return render_template('embroidery_fabric.html')

  return render_template('product.html', name = name)

@app.route('/page/<name>')
def page(name):
  if name=='about_us':
    return render_template('about_us.html')
  elif name=='our_culture':
    return render_template('our_culture.html')
  elif name=='devices':
    return render_template('devices.html')


'''
@app.errorhandler(404)
def page_not_found(e):
  return render_template('404.html'),404

@app.errorhandler(500)
def internal_server_error(e):
  return render_template('500.html'),500
'''
