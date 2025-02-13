from flask import Blueprint, render_template, request, jsonify
from services.products_service import ProductService

product_blueprint = Blueprint('products', __name__)

# ✅ Ruta para servir la interfaz en la raíz
@product_blueprint.route('/')
def index():
    return render_template('index.html')

# ✅ Ruta para agregar un producto (POST)
@product_blueprint.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')

    if not name:
        return jsonify({'error': 'Name is required'}), 400

    new_product = ProductService.create_product(name, description)
    return jsonify({'message': 'Product created', 'id': new_product.id}), 201

# ✅ Ruta para obtener un producto por ID (GET)
@product_blueprint.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    product = ProductService.get_product_by_id(id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    return jsonify({'id': product.id, 'name': product.name, 'description': product.description})

# ✅ Ruta para actualizar un producto (PUT)
@product_blueprint.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')

    if not name:
        return jsonify({'error': 'Name is required'}), 400

    updated_product = ProductService.update_product(id, name, description)
    if not updated_product:
        return jsonify({'error': 'Product not found'}), 404

    return jsonify({'message': 'Product updated successfully'})
