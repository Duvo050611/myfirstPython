from flask import Blueprint, request, jsonify
from controllers.userController import get_all_user, get_user_by_id, create_user, update_user, delete_user

user_bp = Blueprint('users', __name__)

@user_bp.route('/', methods=['GET'])
def index():
    users = get_all_user()
    return jsonify(users), 200

@user_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = get_user_by_id(user_id)
    if not user:
        return jsonify({"error": "Usuario no encontrado"}), 404
    return jsonify(user.to_dict()), 200

@user_bp.route('/', methods=['POST'])
def create():
    data = request.get_json()
    if not data or not data.get('name') or not data.get('email'):
        return jsonify({"error": "Datos inválidos"}), 400
    user = create_user(data)
    return jsonify(user.to_dict()), 201

@user_bp.route('/<int:user_id>', methods=['PUT'])
def update(user_id):
    data = request.get_json()
    user = update_user(user_id, data)
    if not user:
        return jsonify({"error": "Usuario no encontrado"}), 404
    return jsonify(user.to_dict()), 200

@user_bp.route('/<int:user_id>', methods=['DELETE'])
def delete(user_id):
    success = delete_user(user_id)
    if not success:
        return jsonify({"error": "Usuario no encontrado"}), 404
    return jsonify({"message": "Usuario eliminado"}), 200
