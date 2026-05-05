# Importamos la función para manejar plantillas
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/coleccion")
def ver_coleccion():
    # Creamos una lista de diccionarios con datos de prueba
    mis_favoritos = [
        {"nombre": "Revuelto de patatas", "motivo": "Es lo mejor del mundo"},
        {"nombre": "Salmorejo Cordobés", "motivo": "Es muy fresco"},
        {"nombre": "Jamón", "motivo": "Es la tapa perfecta"}
    ]
    # Enviamos la lista completa a la plantilla con el nombre 'items'
    return render_template("galeria.html", favoritos=mis_favoritos)


if __name__ == "__main__":
    # Arrancamos el servidor en modo debug para que se reinicie solo al guardar cambios
    app.run(debug=True)
