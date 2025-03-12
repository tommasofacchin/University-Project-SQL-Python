from main import db
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import or_, func
from typing import List
import models


def add(elem) -> None:
    try:
        db.session.add(elem)
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        print(f"Exception during ADD: {e}")


def add_list(elements: List) -> None:
    try:
        for elem in elements:
            db.session.add(elem)
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        print(f"Exception during ADD_LIST: {e}")


def update() -> None:
    try:
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        print(f"Exception during UPDATE: {e}")


def delete(elem) -> None:
    try:
        db.session.delete(elem)
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        print(f"Exception during DELETE: {e}")


# --- GETTERS ---

def get_users() -> List[models.User]:
    try:
        return (
                db.session.query(models.User)
                .all()
            )
    except SQLAlchemyError as e:
        print(f"Exception during GET_USERS: {e}")


def get_user(*args) -> models.User:
    try:
        query = db.session.query(models.User)

        if args:
            query = query.filter(*args)

        return query.one()
    except SQLAlchemyError as e:
        print(f"Exception during GET_USER: {e}")


def get_cart(user_id: int):
    try:
        return (
                db.session.query(models.Cart)
                .join(models.Product, models.Cart.fk_product == models.Product.id)
                .filter(models.Cart.fk_user == user_id)
                .all()
            )
    except SQLAlchemyError as e:
        print(f"Exception during GET_CART: {e}")


def get_cartDetail(user_id: int, product_id: int) -> models.Cart:
    try:
        return (
                db.session.query(models.Cart)
                .filter(models.Cart.fk_user == user_id,
                        models.Cart.fk_product == product_id)
                .one()
            )
    except SQLAlchemyError as e:
        print(f"Exception during GET_CART_DETAIL: {e}")


def get_cart_total(user_id: int):
    try:
        return (
                db.session.query(func.sum(models.Product.price * models.Cart.quantity))
                .join(models.Cart, models.Product.id == models.Cart.fk_product)
                .filter(models.Cart.fk_user == user_id)
                .scalar()
            )
    except SQLAlchemyError as e:
        print(f"Exception during GET_CART_TOTAL: {e}")


def get_orders(user_id: int):
    try:
        return (
                db.session.query(models.Order)
                .join(models.Status, models.Order.fk_status == models.Status.id)
                .filter(models.Order.fk_user == user_id)
                .all()
            )
    except SQLAlchemyError as e:
        print(f"Exception during GET_ORDERS: {e}")


def get_order(order_id: int):
    try:
        return (
                db.session.query(models.Order)
                .filter(models.Order.id == order_id)
                .one()
            )
    except SQLAlchemyError as e:
        print(f"Exception during GET_ORDER: {e}")


def get_orderDetails(order_id: int):
    try:
        return (
                db.session.query(models.OrderDetail)
                .join(models.Product, models.OrderDetail.fk_product == models.Product.id)
                .filter(models.OrderDetail.fk_order == order_id)
                .all()
            )
    except SQLAlchemyError as e:
        print(f"Exception during GET_ORDER_DETAILS: {e}")


def get_orderDetail(order_id: int, product_id: int) -> models.OrderDetail:
    try:
        return (
                db.session.query(models.OrderDetail)
                .filter(models.OrderDetail.fk_order == order_id,
                        models.OrderDetail.fk_product == product_id)
                .one()
            )
    except SQLAlchemyError as e:
        print(f"Exception during GET_ORDER_DETAIL: {e}")


def get_ordersRecap(user_id: int) -> List[models.OrderRecap]:
    try:
        return (
                db.session.query(models.OrderRecap)
                .filter(models.OrderRecap.fk_user == user_id)
                .order_by(models.OrderRecap.id.desc())
                .all()
            )
    except SQLAlchemyError as e:
        print(f"Exception during GET_ORDER_RECAP: {e}")


def get_orderRecap(order_id: int) -> models.OrderRecap:
    try:
        return (
                db.session.query(models.OrderRecap)
                .filter(models.OrderRecap.id == order_id)
                .one()
            )
    except SQLAlchemyError as e:
        print(f"Exception during GET_ORDER_RECAP: {e}")


def get_ordersSeller(seller_id: int) -> List[models.OrderSeller]:
    try:
        return (
                db.session.query(models.OrderSeller)
                .filter(models.OrderSeller.seller_id == seller_id)
                .order_by(models.OrderSeller.id.desc())
                .all()
            )
    except SQLAlchemyError as e:
        print(f"Exception during GET_ORDERS_SELLER: {e}")


def get_orderSeller(seller_id: int, order_id: int) -> models.OrderSeller:
    try:
        return (
                db.session.query(models.OrderSeller)
                .filter(
                    models.OrderSeller.seller_id == seller_id,
                    models.OrderSeller.id == order_id
                )
                .one()
            )
    except SQLAlchemyError as e:
        print(f"Exception during GET_ORDER_SELLER: {e}")


def get_orderDetailsSeller(seller_id: int, order_id: int):
    try:
        return (
                db.session.query(models.OrderDetail)
                .join(models.Product, models.OrderDetail.fk_product == models.Product.id)
                .join(models.Order, models.OrderDetail.fk_order == models.Order.id)
                .join(models.User, models.Order.fk_user == models.User.id)
                .filter(models.Product.fk_seller == seller_id, models.Order.id == order_id)
                .all()
            )
    except SQLAlchemyError as e:
        print(f"Exception during GET_ORDER_DETAILS_SELLER: {e}")


def get_categories() -> List[models.Category]:
    try:
        return (
                db.session.query(models.Category)
                .all()
            )
    except SQLAlchemyError as e:
        print(f"Exception during GET_CATEGORIES: {e}")


def get_category(id: int) -> models.Category:
    try:
        return (
                db.session.query(models.Category)
                .filter(models.Category.id == id)
                .one()
            )
    except SQLAlchemyError as e:
        print(f"Exception during GET_CATEGORY: {e}")


def get_brands(category_id: int = None) -> List[models.Brand]:
    try:
        query = db.session.query(models.Brand)

        if category_id:
            query = query.filter(models.Brand.fk_category == category_id)

        return query.all()
    except SQLAlchemyError as e:
        print(f"Exception during GET_BRANDS: {e}")


def get_products(*args, n: int = None, order_asc: bool = None):
    try:
        query = (
                db.session.query(models.Product)
                .join(models.Category, models.Product.fk_category == models.Category.id)
                .join(models.User, models.Product.fk_seller == models.User.id)
            )

        if args:
            query = query.filter(*args)

        if n:
            query = query.order_by(func.random()).limit(n)

        if order_asc is not None:
            if order_asc:
                query = query.order_by(models.Product.price.asc())
            else:
                query = query.order_by(models.Product.price.desc())

        return query.all()
    except SQLAlchemyError as e:
        print(f"Exception during GET_PRODUCTS: {e}")


def get_product(product_id: int) -> models.Product:
    try:
        return (
                db.session.query(models.Product)
                .filter(models.Product.id == product_id)
                .one()
            )
    except SQLAlchemyError as e:
        print(f"Exception during GET_PRODUCT: {e}")


def get_statuses():
    try:
        return (
                db.session.query(models.Status)
                .all()
            )
    except SQLAlchemyError as e:
        print(f"Exception during GET_STATUESES: {e}")


def search_products(keyword: str, *args, order_asc: bool = None):
    try:
        query = (
                db.session.query(models.Product)
                .join(models.Category, models.Product.fk_category == models.Category.id)
                .join(models.User, models.Product.fk_seller == models.User.id)
                .filter(
                    or_(
                        models.Product.name.contains(keyword),
                        models.Product.description.contains(keyword),
                        models.Product.brand.contains(keyword),
                        models.Category.description.contains(keyword),
                        models.User.firstname.contains(keyword),
                        models.User.lastname.contains(keyword),
                        models.User.email.contains(keyword),
                    )
                )
            )

        if args:
            query = query.filter(*args)

        if order_asc is not None:
            if order_asc:
                query = query.order_by(models.Product.price.asc())
            else:
                query = query.order_by(models.Product.price.desc())

        return query.all()
    except SQLAlchemyError as e:
        print(f"Exception during SEARCH_PRODUCTS: {e}")
