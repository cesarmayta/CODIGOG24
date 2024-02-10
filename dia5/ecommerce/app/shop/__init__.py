from flask import Blueprint

shop = Blueprint('shop',__name__,url_prefix='/')

@shop.route('/shop')
def index():
    return '<h1>shop</h1>'