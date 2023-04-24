from flask import Flask, request
from PIL import Image
import pytesseract
import argparse
import cv2
import re
import enchant

app = Flask(__name__)

@app.route('/', methods=['POST'])
def upload_file():
    # Obtener la imagen enviada desde el cliente
    image_file = request.files['image']

    filename = image_file.filename

    # Leer la imagen en un objeto de imagen de Pillow
    image = Image.open(image_file)

    # Guardar la imagen en el servidor
    image.save(image_file.filename)

    text = ocr(filename)

    analisis = analizar_str(text)
    

    # Retornar una respuesta al cliente
    # return analisis
    return {
        "validation": 'ok', # 'ko', 'warning'
        "message": "El mensaje es de Bankia y el remitente es sospechoso",
        "text": text
    }

def ocr(imagePath):
    image = cv2.imread(imagePath)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    text = pytesseract.image_to_string(image)
    print(text)
    return text

def extract_emails(text):
    return re.findall('\S+@\S+', text)

def analizar_str(text):
    emails = extract_emails(text)
    palabras = text.split()
    errores = []
    url_dudoso = False
    
    # Analizar cada palabra en busca de errores ortográficos

    
    # Comprobar si hay errores y URL dudoso
    if len(errores) == 0 and not url_dudoso and extract_emails(text):
        return "OK - El filtro ha pasado sin detectar errores."
    elif len(errores) > 0 or not extract_emails(text):
        return "KO - El texto contiene errores ortográficos o la dirección de correo electrónico es incorrecta. Por favor, no haga clic en la URL y elimine el correo."
    else:
        return "WARNING! - El filtro ha detectado errores ortográficos en el texto. Por favor, revise cuidadosamente. "

if __name__ == '__main__':
    app.run(debug=True)