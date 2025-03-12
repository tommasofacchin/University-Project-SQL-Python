from main import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, Integer, String, Numeric, Boolean
from flask_login import UserMixin


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    firstname: Mapped[str] = mapped_column(String(100))
    lastname: Mapped[str] = mapped_column(String(100))
    birthdate: Mapped[str] = mapped_column(String(8))
    email: Mapped[str] = mapped_column(String(100), unique=True)
    pwhash: Mapped[str] = mapped_column(String(60))
    imgpath: Mapped[str] = mapped_column(String(200), nullable=True)
    address: Mapped[str] = mapped_column(String(100), nullable=True)
    zipcode: Mapped[str] = mapped_column(String(10), nullable=True)
    city: Mapped[str] = mapped_column(String(100), nullable=True)
    country: Mapped[str] = mapped_column(String(100), nullable=True)
    seller: Mapped[bool] = mapped_column(Boolean, default=False)

    def __repr__(self):
        return f'''
                id: {self.id},
                firstname: {self.firstname},
                lastname: {self.lastname},
                birthdate: {self.birthdate},
                email: {self.email},
                pwhash: {self.pwhash},
                imgpath: {self.imgpath},
                address: {self.address},
                zipcode: {self.zipcode},
                city: {self.city},
                country: {self.country},
                seller: {self.seller}\n'''


class Category(db.Model):
    __tablename__ = 'categories'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    description: Mapped[str] = mapped_column(String(100))

    def __repr__(self):
        return f'''
                id: {self.id},
                description: {self.description})\n'''


class Product(db.Model):
    __tablename__ = 'products'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(500), nullable=True)
    brand: Mapped[str] = mapped_column(String(100))
    fk_seller: Mapped[int] = mapped_column(Integer, ForeignKey("users.id", ondelete='CASCADE'))
    fk_category: Mapped[int] = mapped_column(Integer, ForeignKey("categories.id"))
    price: Mapped[float] = mapped_column(Numeric(precision=10, scale=2))
    availability: Mapped[int] = mapped_column(Integer)
    imgpath: Mapped[str] = mapped_column(String(200), nullable=True)
    seller = db.relationship('User', lazy='subquery')
    category = db.relationship('Category', lazy='subquery')

    def __repr__(self):
        return f'''
                id: {self.id},
                name: {self.name},
                description: {self.description},
                brand: {self.brand},
                fk_seller: {self.fk_seller},
                fk_category: {self.fk_category},
                price: {self.price},
                availability: {self.availability})\n'''


class Cart(db.Model):
    __tablename__ = 'carts'
    fk_user: Mapped[int] = mapped_column(Integer, ForeignKey("users.id", ondelete='CASCADE'), primary_key=True)
    fk_product: Mapped[int] = mapped_column(Integer, ForeignKey("products.id", ondelete='CASCADE'), primary_key=True)
    quantity: Mapped[int] = mapped_column(Integer)
    product = db.relationship('Product', lazy='subquery')

    def __repr__(self):
        return f'''
                fk_user: {self.fk_user},
                fk_product: {self.fk_product},
                quantity: {self.quantity}\n'''


class Status(db.Model):
    __tablename__ = 'statuses'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    description: Mapped[str] = mapped_column(String(100))

    def __repr__(self):
        return f'''
                id: {self.id},
                description: {self.description}\n'''


class Order(db.Model):
    __tablename__ = 'orders'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fk_user: Mapped[int] = mapped_column(Integer, ForeignKey("users.id", ondelete='CASCADE'))
    fk_status: Mapped[int] = mapped_column(Integer, ForeignKey("statuses.id"))
    date: Mapped[str] = mapped_column(String(8))
    address: Mapped[str] = mapped_column(String(100))
    zipcode: Mapped[str] = mapped_column(String(10))
    city: Mapped[str] = mapped_column(String(100))
    country: Mapped[str] = mapped_column(String(100))
    status = db.relationship('Status', lazy='subquery')

    def __repr__(self):
        return f'''
                id: {self.id},
                fk_user: {self.fk_user},
                fk_status: {self.fk_status},
                date: {self.date}
                address: {self.address}
                zipcode: {self.zipcode}
                city: {self.city}
                country: {self.country}\n'''


class OrderDetail(db.Model):
    __tablename__ = 'order_details'
    fk_order: Mapped[int] = mapped_column(Integer, ForeignKey("orders.id", ondelete='CASCADE'), primary_key=True)
    fk_product: Mapped[int] = mapped_column(Integer, ForeignKey("products.id"), primary_key=True)
    quantity: Mapped[int] = mapped_column(Integer)
    order = db.relationship('Order', lazy='subquery')
    product = db.relationship('Product', lazy='subquery')

    def __repr__(self):
        return f'''
                fk_order: {self.fk_order},
                fk_product: {self.fk_product},
                quantity: {self.quantity}\n'''


# ----- VIEWs -----

class OrderRecap(db.Model):
    __tablename__ = 'orders_recap'
    __table_args__ = {'info': dict(is_view=True)}
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fk_user: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    date: Mapped[str] = mapped_column(String(8))
    address: Mapped[str] = mapped_column(String(100))
    zipcode: Mapped[str] = mapped_column(String(10))
    city: Mapped[str] = mapped_column(String(100))
    country: Mapped[str] = mapped_column(String(100))
    status: Mapped[str] = mapped_column(String(100))
    items: Mapped[int] = mapped_column(Integer)
    total: Mapped[float] = mapped_column(Numeric(precision=10, scale=2))

    def __repr__(self):
        return f'''
                id: {self.id}
                fk_user: {self.fk_user}
                date: {self.date}
                address: {self.address}
                zipcode: {self.zipcode}
                city: {self.city}
                country: {self.country}
                status: {self.status}
                items: {self.items}
                total: {self.total}\n'''


class OrderSeller(db.Model):
    __tablename__ = 'orders_sellers'
    __table_args__ = {'info': dict(is_view=True)}
    seller_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fk_user: Mapped[int] = mapped_column(Integer)
    firstname: Mapped[str] = mapped_column(String(100))
    lastname: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(100), unique=True)
    date: Mapped[str] = mapped_column(String(8))
    address: Mapped[str] = mapped_column(String(100))
    zipcode: Mapped[str] = mapped_column(String(10))
    city: Mapped[str] = mapped_column(String(100))
    country: Mapped[str] = mapped_column(String(100))
    status: Mapped[str] = mapped_column(String(100))
    items: Mapped[int] = mapped_column(Integer)
    total: Mapped[float] = mapped_column(Numeric(precision=10, scale=2))

    def __repr__(self):
        return f'''
                seller_id: {self.seller_id}
                order_id: {self.order_id}
                fk_user: {self.fk_user}
                firstname: {self.firstname}
                lastname: {self.lastname}
                email: {self.email}
                date: {self.date}
                address: {self.address}
                zipcode: {self.zipcode}
                city: {self.city}
                country: {self.country}
                status: {self.status}
                items: {self.items}
                total: {self.total}\n'''


class Brand(db.Model):
    __tablename__ = 'brands'
    __table_args__ = {'info': dict(is_view=True)}
    brand: Mapped[str] = mapped_column(String(100), primary_key=True)
    fk_category: Mapped[int] = mapped_column(Integer, ForeignKey("categories.id"), nullable=True)

    def __repr__(self):
        return f'''
                brand: {self.brand}
                fk_category: {self.fk_category}\n'''
