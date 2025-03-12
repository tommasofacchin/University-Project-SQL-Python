from flask import Blueprint, render_template, request, jsonify
from flask_login import current_user

home = Blueprint('home', __name__,  template_folder='templates',
                 static_folder='static')


@home.route("/", methods=['GET', 'POST'])
def index():
    from db_helper import get_categories
    categories = get_categories()
    categories_links = [
            (elem.description, f"/home/category_page/{elem.id}") for elem in categories
        ]

    products = None

    if request.method == 'POST' and 'btn-search' in request.form:
        from db_helper import search_products
        products = search_products(request.form.get('searchbar'))
    else:
        from db_helper import get_products
        products = get_products(n=8)

    # GET request
    if current_user.is_authenticated:
        return render_template(
                'index.html',
                products=products,
                categories=categories_links,
                user=current_user
            )

    return render_template(
            'index.html',
            products=products,
            categories=categories_links,
        )


@home.route("/category_page/<int:category_id>/<string:brand>", methods=['GET', 'POST'])
@home.route("/category_page/<int:category_id>", methods=['GET', 'POST'])
def category_page(category_id, brand=None):
    # Imports
    from db_helper import get_category, get_brands
    from models import Product

    category = get_category(category_id)
    brands = get_brands(category_id)
    brands_links = [
            (elem.brand, f"/home/category_page/{category_id}/{elem.brand}") for elem in brands
        ]

    products = None

    if 'btn-search' in request.form:
        from db_helper import search_products
        products = search_products(
                request.form.get('searchbar'),
                Product.fk_category == category_id,
                *(Product.brand == brand,) if brand is not None else ()
            )
    else:
        from db_helper import get_products
        products = get_products(
                Product.fk_category == category_id,
                *(Product.brand == brand,) if brand is not None else ()
            )

    # GET request
    if current_user.is_authenticated:
        return render_template(
                'category.html',
                category=category,
                brand=brand,
                brands=brands_links,
                products=products,
                user=current_user
            )

    return render_template(
            'category.html',
            category=category,
            brand=brand,
            brands=brands_links,
            products=products,
        )


@home.route('/send_id', methods=['POST'])
def send_id():
    if request.is_json:
        product_id = request.json.get('id')

        if current_user.is_authenticated:
            from db_helper import add, update, get_cartDetail, get_product
            from models import Cart
            cartDetail = get_cartDetail(current_user.id, product_id)

            qt = 1
            if cartDetail:
                qt += cartDetail.quantity

            if qt > get_product(product_id).availability:
                return jsonify({"status": "success", "quantity": 0})

            if cartDetail:
                cartDetail.quantity += 1
                update()
            else:
                cartDetail = Cart(
                        fk_user=current_user.id,
                        fk_product=product_id,
                        quantity=1
                    )
                add(cartDetail)

            return jsonify({"status": "success", "quantity": cartDetail.quantity})

        return jsonify({"status": "success"})

    else:
        return jsonify({"error": "Invalid content type"}), 415
