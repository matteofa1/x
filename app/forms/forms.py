from flask_wtf import Form 
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

class RegisterForm(Form):
	correo = StringField('Correo', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])

class ProductoForm(Form):
	producto = StringField('Nombre de producto', validators=[DataRequired()])