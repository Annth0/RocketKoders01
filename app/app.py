# Se debe tener instalado el Flask en el terminal
# pip install Flask - python app\app.py runserver

from re import A
from flask import Flask, render_template, request

app = Flask(__name__)


@app.before_request
def before_request():
    print('Antes de la petición')


@app.after_request
def after_request(response):
    print('Después de la petición')
    return response


""" @app.route('/')
def index():
    return "Rockert Koders 1"
"""


def index():
    print('Realizando la petición')
    # establecer pagina principal o mensaje solito
    # return "Bienvenido a la pagina principal del Koder Anthonn - de prueba."
    # establecer configuracion de plantilla (template)
    # return render_template('index.html', titulo='Página principal de prueba')
    data = {
        'titulo': 'Index',
        'encabezado': 'Bienvenido!',
    }
    return render_template('index.html', data=data)


@app.route('/holamundo')
def hola_mundo():
    return "Hola Mundo!"


@app.route('/contacto')
def contacto():
    data = {
        'titulo': 'Contacto',
        'encabezado': 'Bienvenido! (a)',
    }
    return render_template('contacto.html', data=data)

# ___________________________________
# comportamiento dinamico

# @app.route('/saludo')
# def saludo():
#    return 'Hola Koder!'  | normaal
# Parametro que forma parte de la ruta


@app.route('/saludo/<nombre>')
def saludo(nombre):
    return 'Hola, {0}!'.format(nombre)
# ------------------------------------


@app.route('/suma/<int:valor1>/<int:valor2>')
def suma(valor1, valor2):
    # error de tipo porque no puede resultar solo entero
    #  return valor1 + valor2 _________solución abajo
    return 'la suma es: {0}!'.format((valor1 + valor2))
# ------------------------------------
# Combinar parametros desde ruta


@app.route('/perfil/<nombre>/<int:edad>')
def perfil(nombre, edad):
    return 'Hola, tu nombre es {0}, y tu edad es {1}!. Bienvenid@'.format(nombre, edad)
# ------------------------------------
# Mostrar distindos datos en las plantillas


@app.route('/lenguajes')
def lenguajes():
    data = {
        'hay_lenguajes': True,
        'lenguajes': ['PHP', 'Python', 'Kotlin', 'Java', 'C#', 'JavaScript']
    }
    return render_template('lenguajes.html', data=data)
# ___________________________________

# HTTP: Hypertext Transfer Protocol
# GET, POST, PUT, DELETE.


@app.route('/datos')
def datos():
    a = request.args.get('valor1')
    b = int(request.args.get('valor2'))
    c = request.args.get('valor3')
# impresion en consola de los elementos de la petición - enlace
    # print(request.args)
    # en navegador va: http://127.0.0.1:5005/datos?valor1=pepe
    # # en navegador va: http://127.0.0.1:5005/datos?valor1=pepe&valor2=23&valor3=sandías
    # en donde después del signo ? se añade lo que estamos obteniendo para mostrar en la página
    '''obtener el valor que contenga el arggumento con llave que ahora tiene nombre valor1 pero se puede cambiar y poner más llaves, se pueden poner mas concatenando con el simbolo &'''
    return 'Estos son los datos: nombre {0}, edad: {1}, gusta: {2}'.format(a, b, c)


# se implementam reglas de flask para que el entorno se actualice automaticamente y no se tenga que cerrar y abrir a cada momento el servidor
# el app.run(debug=True, port=5005) indica que habilite el modo debug (automaticos cambios) y podemos establecer un puerto personalizado
if __name__ == '__main__':
    app.add_url_rule('/', view_func=index)
    app.run(debug=True, port=5005)


#  shift + alt + f - formatear
