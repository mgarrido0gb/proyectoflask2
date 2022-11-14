from flask import Flask, jsonify
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

#@app.route('/', methods=['GET'])
#def inicio():
#    return jsonify({"response":"Hola Mundo"})

sitioweb = 'https://www.culturagenial.com/es/peliculas-recomendadas/'
respuesta = requests.get(sitioweb)
contenido =respuesta.text

#localizar elementos en una pagina web
soup =  BeautifulSoup(contenido,'lxml')
#print(soup.prettify())

caja = soup.find('article',class_='article')

titulo = caja.find('h3').get_text()
transcript = caja.find('h3').get_text(strip=True, separator=' ')
print(titulo)
with open(f'{titulo}.txt', 'w', encoding='utf-8') as file:
    file.write(transcript)
 

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=4000,debug=True) 