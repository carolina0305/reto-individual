from flask import Flask, jsonify

app = Flask(__name__)

# Asumimos un año de nacimiento para el "asistente" y un nombre para mostrar.
# Si el número en la URL coincide con este año, devolvemos el mensaje HTML pedido.
# Nota: Estoy asumiendo el año 2008 — si quieres otro año, dímelo y lo cambio.
BIRTH_YEAR = 2008
ASSISTANT_NAME = "Carolina"


@app.route('/validar/<int:codigo>')
def validar(codigo: int):
	"""Ruta dinámica que valida si `codigo` coincide con el año de nacimiento.

	- Si coincide: devuelve HTML con 'Acceso concedido a [Carolina]'.
	- Si no coincide: devuelve JSON con el código recibido.
	"""
	if codigo == BIRTH_YEAR:
		# Devolvemos HTML explícito
		return f"<h1>Acceso concedido a {ASSISTANT_NAME}</h1>", 200, {"Content-Type": "text/html; charset=utf-8"}
	return "<h1>Código erróneo</h1><p>Inténtelo de nuevo.</p>", 200, {"Content-Type": "text/html; charset=utf-8"}


if __name__ == '__main__':
	# Ejecuta el servidor sólo cuando se ejecuta el script directamente.
	# No arrancamos el servidor al importar el módulo (útil para pruebas).
	app.run(host='0.0.0.0', port=5000, debug=True)
