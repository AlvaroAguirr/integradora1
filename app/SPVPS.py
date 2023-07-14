from flask import Flask

#importar views
from views.home_views import home_views
from views.product_view import product_views
from views.report_views import report_views
from views.user_views import user_views


app = Flask(__name__)
app.config['SECRET_KEY'] = 'My secret key'

#registrar views
app.register_blueprint(home_views)
app.register_blueprint(product_views)
app.register_blueprint(report_views)
app.register_blueprint(user_views)

if __name__ =='__main__':
    app.run(debug =True)  