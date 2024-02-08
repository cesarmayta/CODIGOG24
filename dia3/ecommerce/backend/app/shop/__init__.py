from flask import Blueprint,jsonify

shop = Blueprint('shop',__name__,url_prefix='/')

@shop.route('/')
def index():
    context = {
        'message':'prueba de endpoint'
    }
    return jsonify(context)
    