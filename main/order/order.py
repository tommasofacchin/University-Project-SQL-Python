from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required
from decorators import check_order_owner, check_order_seller, seller_required

order = Blueprint('order', __name__,  template_folder='templates',
                  static_folder='static')


@order.route("/order/<int:order_id>", methods=['GET', 'POST'])
@login_required
@check_order_owner
def order_page(order_id: int):
    # GET request
    from db_helper import get_orderRecap, get_orderDetails
    return render_template(
            'order.html',
            user=current_user,
            order=get_orderRecap(order_id),
            orderDetails=get_orderDetails(order_id)
        )


@order.route("/order_seller/<int:order_id>", methods=['GET', 'POST'])
@login_required
@seller_required
@check_order_seller
def order_page_seller(order_id: int):
    if request.method == 'POST':
        status_id = request.form.get("status_id")

        if status_id is not None:
            from db_helper import get_order, update
            get_order(order_id).fk_status = status_id
            update()

        return redirect(url_for('profile.profile_page'))

    # GET request
    from db_helper import get_orderSeller, get_orderDetailsSeller, get_statuses
    return render_template(
            'order.html',
            user=current_user,
            order=get_orderSeller(current_user.id, order_id),
            orderDetails=get_orderDetailsSeller(current_user.id, order_id),
            statuses=get_statuses()
        )
