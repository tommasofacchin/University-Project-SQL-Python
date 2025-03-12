from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from flask_login import current_user, login_required


cart = Blueprint('cart', __name__,  template_folder='templates',
                 static_folder='static')


@cart.route('/cart', methods=['GET', 'POST'])
def cart_page():
    if request.method == 'POST':
        if current_user.is_authenticated:
            return redirect(url_for('cart.checkout_page'))
        else:
            return redirect(url_for('auth.login'))

    # GET request
    if current_user.is_authenticated:
        from db_helper import get_cart
        cart = get_cart(current_user.id)

        return render_template('cart.html', cart=cart, user=current_user)

    return render_template('cart.html')


@cart.route("/checkout", methods=['GET', 'POST'])
@login_required
def checkout_page():
    if request.method == 'POST':
        from db_helper import add
        from models import Order
        from datetime import datetime

        order = Order(
                fk_user=current_user.id,
                date=(datetime.now()).strftime("%Y%m%d"),
                fk_status=1,
                address=request.form.get('address'),
                zipcode=request.form.get('zip'),
                city=request.form.get('city'),
                country=request.form.get('state')
            )

        add(order)
        return redirect(url_for('home.index'))

    # GET request
    from db_helper import get_cart, get_cart_total
    from decimal import Decimal, ROUND_DOWN

    cart = get_cart(current_user.id)
    subtotal = get_cart_total(current_user.id)
    fee = Decimal(4.99).quantize(Decimal('0.00'), rounding=ROUND_DOWN)
    total = subtotal + fee

    return render_template(
            'checkout.html',
            user=current_user,
            cart=cart,
            subtotal=subtotal,
            fee=fee,
            total=total
        )


@cart.route('/send_id', methods=['POST'])
def send_id():
    if request.is_json:
        product_id = request.json.get('id')

        if current_user.is_authenticated:
            from db_helper import delete, get_cartDetail
            delete(get_cartDetail(current_user.id, product_id))

        return jsonify({"status": "success", "product_id": product_id})

    else:
        return jsonify({"error": "Invalid content type"}), 415


@cart.route('/send_qt', methods=['POST'])
def send_qt():
    if request.is_json:
        product_id = request.json.get('id')
        qt = request.json.get('qt')

        if current_user.is_authenticated and qt > 0:
            from db_helper import get_cartDetail, get_product, update

            if get_product(product_id).availability < qt:
                return jsonify({"status": "success", "product_id": product_id, "status": "unavailable"})

            cartDetail = get_cartDetail(current_user.id, product_id)
            cartDetail.quantity = qt
            update()

        return jsonify({"status": "success", "product_id": product_id})

    else:
        return jsonify({"error": "Invalid content type"}), 415
