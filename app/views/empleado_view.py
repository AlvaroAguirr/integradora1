from flask import Blueprint, render_template


empleado_views = Blueprint ('personal',__name__)

@empleado_views.route("/emm/")
def emp():
    return render_template('empleado/empleados.html')

@empleado_views.route("/Añadir-empleado/")
def a_emp():
    return render_template("/empleado/creat-personal.html")