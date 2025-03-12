from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required
from decorators import seller_required, check_product_owner


product = Blueprint('product', __name__,  template_folder='templates',
                    static_folder='static')


@product.route("/product/<int:product_id>", methods=['GET', 'POST'])
@product.route("/product", methods=['GET', 'POST'])
@login_required
@seller_required
@check_product_owner
def product_page(product_id=None):
    # Imports
    from db_helper import get_categories, add
    from models import Product

    if request.method == 'POST':
        product = Product(
                name=request.form.get('product_name'),
                description=request.form.get('product_description'),
                brand=request.form.get('product_brand'),
                fk_category=request.form.get('product_category'),
                imgpath='',
                fk_seller=current_user.id
            )

        error_templ = render_template(
                'product.html',
                user=current_user,
                categories=get_categories(),
                error='Invalid image extensions, price or availability'
            )

        # Try to convert price
        try:
            price = request.form.get('product_price'),
            tmp = float(price[0])
            product.price = tmp
        except ValueError:
            return error_templ

        # Try to convert availability
        try:
            availability = request.form.get('product_availability'),
            tmp = int(availability[0])
            product.availability = tmp
        except ValueError:
            return error_templ

        # Save image
        if 'product_image' in request.files:
            from utils import allowed_file
            img = request.files['product_image']

            if allowed_file(img.filename):
                from os import path
                from datetime import datetime
                current_time = (datetime.now()).strftime("%Y%m%d%H%M%S")
                dir = path.join(path.dirname(path.abspath(__file__)), 'static/images')
                imgname = f"{current_time}.png"
                img.save(path.join(dir, imgname))
                product.imgpath = f"images/{imgname}"
            elif product_id is None:
                return error_templ

        if product_id is not None:
            from db_helper import get_product, update
            current_product = get_product(product_id)

            if not product.imgpath:
                product.imgpath = current_product.imgpath

            current_product.imgpath = product.imgpath
            current_product.name = product.name
            current_product.description = product.description
            current_product.brand = product.brand
            current_product.fk_category = product.fk_category
            current_product.price = product.price
            current_product.availability = product.availability
            update()
        else:
            add(product)

        return redirect(url_for('profile.profile_page'))

    # GET request
    product = None
    if product_id is not None:
        from db_helper import get_product
        product = get_product(product_id)

    return render_template(
            'product.html',
            user=current_user,
            categories=get_categories(),
            product=product
        )


@product.route("/product_list", methods=['GET', 'POST'])
@login_required
@seller_required
def product_list_page():
    from db_helper import get_categories, get_products
    from models import Product

    return render_template(
            'product_list.html',
            user=current_user,
            categories=get_categories(),
            products=get_products(Product.fk_seller == current_user.id)
        )


@product.route("/product_view/<int:product_id>", methods=['GET', 'POST'])
def product_view_page(product_id: int):
    from db_helper import get_product
    return render_template(
            'product_view.html',
            user=current_user,
            product=get_product(product_id)
        )
