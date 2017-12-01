from dashButtonBasic import dashButton

def saluta(asd):
	print("ciao")

pulsante=dashButton("<your dashbutton mac>", saluta)

pulsante.startListening()
