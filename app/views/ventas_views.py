from flask import Blueprint, render_template

ventas_views =Blueprint ('venta', __name__)

@ventas_views.route ('/ventt/')
def vender():
    return render_template('ventas/ventas.html')