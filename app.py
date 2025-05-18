from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    resultado = None
    if request.method == "POST":
        nombre = request.form["nombre"]
        edad = int(request.form["edad"])
        cantidad = int(request.form["cantidad"])

        precio_unitario = 9000
        total_sin_descuento = precio_unitario * cantidad

        if edad < 18:
            descuento = 0
        elif 18 <= edad <= 30:
            descuento = 0.15
        else:
            descuento = 0.25

        monto_descuento = total_sin_descuento * descuento
        total_con_descuento = total_sin_descuento - monto_descuento

        resultado = {
            "nombre": nombre,
            "total_sin_descuento": total_sin_descuento,
            "monto_descuento": monto_descuento,
            "total_con_descuento": total_con_descuento
        }

    return render_template("ejercicio1.html", resultado=resultado)


@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():

    mensaje = None

    if request.method == "POST":
        nombre = request.form["nombre"]
        clave = request.form["clave"]

        if nombre == "juan" and clave == "admin":
            mensaje = "Bienvenido administrador juan"
        elif nombre == "pepe" and clave == "user":
            mensaje = "Bienvenido usuario pepe"
        else:
            mensaje = "Nombre de usuario o contraseña incorrectos"

    return render_template("/ejercicio2.html", mensaje=mensaje)


if __name__ == "__main__":
    app.run(debug=True)
