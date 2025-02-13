from flask import Flask, render_template
from models.products import db
from controllers.product_controller import product_blueprint

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:123@172.17.0.2:3306/swarch2024ii_db'

db.init_app(app)
app.register_blueprint(product_blueprint)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
