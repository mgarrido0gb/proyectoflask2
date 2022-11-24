FROM python:3.7.0-slim

ENV TZ=America/Santiago


#CREAR CARPETA LLAMADA APP
WORKDIR /app
COPY . /app

#Instalando Python y PIP Última versión
RUN  pip install --upgrade pip
#leer archivos del requeriments.txt e instalarlos
RUN pip install -r requirements.txt



#EJECUTAMOS LA APLICACIÓN"
CMD ["python","app.py"]