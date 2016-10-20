from app import app
from flask import render_template
from forms.forms import ProductoForm 
from quotes_spider import QuotesSpider 
import pyrebase

def firebaseObject():
	config = {
	"apiKey": "AIzaSyC9vEDMe5pYkqLNcuQUEroXSu1bxTHfqR8",
	"authDomain":"demoflask-26215.firebaseapp.com",
	"databaseURL": "https://demoflask-26215.firebaseio.com",
	"storageBucket": "demoflask-26215.appspot.com"
	}
	firebase = pyrebase.initialize_app(config)

	return firebase

@app.route("/", methods=('GET', 'POST'))
def busqueda():
	fbase = firebaseObject()
	auth = fbase.auth()
	user = auth.sign_in_with_email_and_password('paco.ocampor@gmail.com', '41000705')
	db = fbase.database()
	lista = []
	result = db.child("/").get()
	for producto in result.each():
		val = producto.val()
		lista.append(val)
	print(lista)

def scrapy():
	formulario = ProductoForm()
	if formulario.validate_on_submit():
		competencia = QuotesSpider(scrapy.Spider)
		data = competencia{"nombre":formulario.producto.data}
		return data


		#return render_template("/homework", data = result.val(), form=formulario)


	

	#return render_template("resultado.html", producto=lista)

	#formulario = ProductoForm()
	#if formulario.validate_on_submit():
	#	data =  {"nombre":formulario.producto.data}
	#	db.child("SKU").push(data)
	#	return render_template("/producto", data = result.val(), form=formulario)
		



