from functools import wraps
from flask_login import current_user


# Sellers
def seller_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.seller:
            return "Access Denied", 403
        return f(*args, **kwargs)
    return decorated_function


# Order owner
def check_order_owner(f):
    @wraps(f)
    def decorated_function(order_id, *args, **kwargs):
        from db_helper import get_order
        order = get_order(order_id)
        if order and order.fk_user != current_user.id:
            return "Access Denied", 403
        return f(order_id, *args, **kwargs)
    return decorated_function


# Order owner (Seller)
def check_order_seller(f):
    @wraps(f)
    def decorated_function(order_id, *args, **kwargs):
        from db_helper import get_orderSeller
        if not get_orderSeller(current_user.id, order_id):
            return "Access Denied", 403
        return f(order_id, *args, **kwargs)
    return decorated_function


# Product owner
def check_product_owner(f):
    @wraps(f)
    def decorated_function(product_id=None, *args, **kwargs):
        from db_helper import get_product
        if product_id is not None and get_product(product_id).fk_seller != current_user.id:
            return "Access Denied", 403
        return f(product_id, *args, **kwargs)
    return decorated_function
