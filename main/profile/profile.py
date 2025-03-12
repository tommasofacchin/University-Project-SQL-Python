from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required, logout_user

profile = Blueprint('profile', __name__,  template_folder='templates',
                    static_folder='static')


@profile.route("/profile", methods=['GET', 'POST'])
@login_required
def profile_page():
    if request.method == 'POST':
        # Logout request
        if 'btn-logout' in request.form:
            logout_user()
            return redirect(url_for('home.index'))

        current_user.address = request.form.get('address')
        current_user.city = request.form.get('city')
        current_user.country = request.form.get('state')
        current_user.zipcode = request.form.get('zip')

        from db_helper import update
        update()

        return redirect(url_for('home.index'))

    # GET request
    orders = None

    if current_user.seller:
        from db_helper import get_ordersSeller
        orders = get_ordersSeller(current_user.id)
    else:
        from db_helper import get_ordersRecap
        orders = get_ordersRecap(current_user.id)

    return render_template(
            'profile.html',
            user=current_user,
            orders=orders,
        )
