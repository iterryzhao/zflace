from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required,Email

class ContactForm(Form):
  name = StringField(u'Please input your name.', validators = [Required()])
  phone = StringField('phone')
  email = StringField('email', validators = [Required(), Email()])
  msg = TextAreaField('Message',default = 'Please input your message here.', validators = [Required()])
  sbt = SubmitField('Submit')