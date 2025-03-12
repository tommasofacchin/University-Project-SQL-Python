CREATE TABLE users (
        id INTEGER NOT NULL,
        firstname VARCHAR(100) NOT NULL,
        lastname VARCHAR(100) NOT NULL,
        birthdate VARCHAR(8) NOT NULL,
        email VARCHAR(100) NOT NULL,
        pwhash VARCHAR(60) NOT NULL,
        imgpath VARCHAR(200),
        address VARCHAR(100),
        zipcode VARCHAR(10),
        city VARCHAR(100),
        country VARCHAR(100),
        seller BOOLEAN NOT NULL,
        PRIMARY KEY (id),
        UNIQUE (email)
);

CREATE TABLE categories (
        id INTEGER NOT NULL,
        description VARCHAR(100) NOT NULL,
        PRIMARY KEY (id)
);

CREATE TABLE statuses (
        id INTEGER NOT NULL,
        description VARCHAR(100) NOT NULL,
        PRIMARY KEY (id)
);

CREATE TABLE products (
        id INTEGER NOT NULL,
        name VARCHAR(100) NOT NULL,
        description VARCHAR(500),
        brand VARCHAR(100) NOT NULL,
        fk_seller INTEGER NOT NULL,
        fk_category INTEGER NOT NULL,
        price NUMERIC(10, 2) NOT NULL,
        availability INTEGER NOT NULL,
        imgpath VARCHAR(200),
        PRIMARY KEY (id),
        FOREIGN KEY(fk_seller) REFERENCES users (id) ON DELETE CASCADE,
        FOREIGN KEY(fk_category) REFERENCES categories (id)
);

CREATE TABLE orders (
        id INTEGER NOT NULL,
        fk_user INTEGER NOT NULL,
        fk_status INTEGER NOT NULL,
        date VARCHAR(8) NOT NULL,
        address VARCHAR(100) NOT NULL,
        zipcode VARCHAR(10) NOT NULL,
        city VARCHAR(100) NOT NULL,
        country VARCHAR(100) NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY(fk_user) REFERENCES users (id) ON DELETE CASCADE,
        FOREIGN KEY(fk_status) REFERENCES statuses (id)
);

CREATE TABLE carts (
        fk_user INTEGER NOT NULL,
        fk_product INTEGER NOT NULL,
        quantity INTEGER NOT NULL,
        PRIMARY KEY (fk_user, fk_product),
        FOREIGN KEY(fk_user) REFERENCES users (id) ON DELETE CASCADE,
        FOREIGN KEY(fk_product) REFERENCES products (id) ON DELETE CASCADE
);

CREATE TABLE order_details (
        fk_order INTEGER NOT NULL,
        fk_product INTEGER NOT NULL,
        quantity INTEGER NOT NULL,
        PRIMARY KEY (fk_order, fk_product),
        FOREIGN KEY(fk_order) REFERENCES orders (id) ON DELETE CASCADE,
        FOREIGN KEY(fk_product) REFERENCES products (id)
);


CREATE VIEW brands AS
	SELECT DISTINCT brand, fk_category
	FROM products;


CREATE VIEW orders_recap AS
	SELECT o.id, o.fk_user, o.date, o.address, o.zipcode, o.city, o.country, 
			s.description AS status, COUNT(*) AS items, SUM(p.price * od.quantity) AS total
	FROM orders o 
		JOIN statuses s ON o.fk_status = s.id 
		JOIN order_details od ON o.id = od.fk_order
		JOIN products p ON od.fk_product = p.id
	GROUP BY o.id;


CREATE VIEW orders_sellers AS
	SELECT p.fk_seller AS seller_id, o.id, u.id AS fk_user, u.firstname, 
			u.lastname, u.email, o.date, o.address, o.zipcode, o.city, o.country, 
			s.description AS status, COUNT(*) AS items, SUM(p.price * od.quantity) AS total
	FROM orders o 
		JOIN statuses s ON o.fk_status = s.id
		JOIN users u ON o.fk_user = u.id
		JOIN order_details od ON o.id = od.fk_order
		JOIN products p ON od.fk_product = p.id
	GROUP BY p.fk_seller, o.id;


CREATE TRIGGER tr_manage_orders
AFTER INSERT ON orders
FOR EACH ROW
BEGIN

        INSERT INTO order_details(
                fk_order,
                fk_product,
                quantity
        )
        SELECT  NEW.id,
                carts.fk_product,
                carts.quantity
        FROM carts
        WHERE carts.fk_user = NEW.fk_user;


        DELETE FROM carts
        WHERE carts.fk_user = NEW.fk_user;


        UPDATE products
        SET availability = availability - (
                SELECT quantity
                FROM order_details
                WHERE order_details.fk_product = products.id
                        AND order_details.fk_order = NEW.id
        )
        WHERE products.id IN (
                SELECT fk_product
                FROM order_details
                WHERE fk_order = NEW.id
        );  

END;


-- CREATE UNIQUE INDEX idx_users ON users(email); Già creato in automatico da SQLITE
CREATE INDEX idx_products ON products(name, brand, fk_seller);
CREATE INDEX idx_orders ON orders(fk_user);
-- CREATE INDEX idx_order_details ON order_details(fk_order); -- Già creato in automatico da SQLITE
