from flask import (Flask, render_template, url_for,
                   redirect)

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('menu_adm.html')

@app.route("/hola")
def cerrar():
    return render_template('cierreSesion.html')

@app.route("/base")
def Iniciar():
    return render_template('base.html')

@app.route("/products")
def productos():
    return render_template('products.html')
@app.route("/login")
def login():
    return render_template('login.html')

if __name__ =='__main__':
    app.run(debug =True)  