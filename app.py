from flask import Flask, jsonify
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

#@app.route('/', methods=['GET'])
#def inicio():
#    return jsonify({"response":"Hola Mundo"})

sitioweb = 'https://www.bcn.cl/historiapolitica/presidentes_de_la_republica/index.html'
respuesta = requests.get(sitioweb)
contenido =respuesta.text

#localizar elementos en una pagina web
soup =  BeautifulSoup(contenido,'lxml')
#print(soup.prettify())

todo = soup.find_all('div',class_='container')

nombres = soup.find_all('h5',class_='seleccionRS')


titulotxt = list()
for listado in nombres:
    resultado = print(listado.text.replace(' ','|'))
    titulotxt.append(listado.text)
    
todo = list(map(str,titulotxt))
resultado = ''.join(todo)
    
with open('presidentes.txt', 'w', encoding='utf-8') as file:
   file.write(resultado.replace(' ','|'))

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=4000,debug=True) 