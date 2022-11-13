from flask import Flask, jsonify
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

#@app.route('/', methods=['GET'])
#def inicio():
#    return jsonify({"response":"Hola Mundo"})

sitioweb = 'https://subslikescript.com/movie/2012-1190080'
respuesta = requests.get(sitioweb)
contenido =respuesta.text

#localizar elementos en una pagina web
soup =  BeautifulSoup(contenido,'lxml')
#print(soup.prettify())

caja = soup.find('article',class_='main-article')
titulo = caja.find('h1').get_text()

transcript = caja.find('div',class_='full-script').get_text(strip=True, separator=' ')

with open(f'{titulo}.txt', 'w', encoding='utf-8') as file:
    file.write(transcript)
 

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=4000,debug=True) 