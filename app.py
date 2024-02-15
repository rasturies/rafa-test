from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    print("Solicitud recibida en la ruta /")
    return 'Hola Mundo8888!'

if __name__ == '__main__':
    print("Iniciando la aplicación en el puerto 80...")
    app.run(host='0.0.0.0', port=80)

