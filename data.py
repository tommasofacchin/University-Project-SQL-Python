import db_helper as db
import models as md
import random


categories = [
    md.Category(id=1, description='Interior items'),
    md.Category(id=2, description='Sport and travel'),
    md.Category(id=3, description='Jewellery'),
    md.Category(id=4, description='Accessories'),
    md.Category(id=5, description='Automobiles'),
    md.Category(id=6, description='House'),
    md.Category(id=7, description='Music'),
    md.Category(id=8, description='Books'),
    md.Category(id=9, description='Kids'),
    md.Category(id=10, description='Pets'),
    md.Category(id=11, description='Fashion'),
    md.Category(id=12, description='Computers'),
    md.Category(id=13, description='Smartphones'),
    md.Category(id=14, description='Movies'),
    md.Category(id=15, description='Other items')
]

statuses = [
    md.Status(id=1, description='Processing'),
    md.Status(id=2, description='Shipped'),
    md.Status(id=3, description='Delivered'),
    md.Status(id=4, description='Cancelled'),
    md.Status(id=5, description='Returned'),
    md.Status(id=6, description='Pending payment'),
    md.Status(id=7, description='Completed')
]

users = [
    md.User(
        id=1,
        firstname='Ecommerce Company',
        lastname='',
        email='info@ecommercecompany.com',
        birthdate='00000000',
        pwhash='$2b$12$d1PTgoG9EUpebdrArF.v0eORHDq8yEyNgXSJbPv5cPl.VteP3UYyK',
        address='123 Main St',
        zipcode='12345',
        city='Anytown',
        country='Countryland',
        seller=True
    ),
    md.User(
        id=2,
        firstname='Luigi',
        lastname='Verdi',
        email='luigi.verdi@email.com',
        birthdate='02021990',
        pwhash='$2b$12$d1PTgoG9EUpebdrArF.v0eORHDq8yEyNgXSJbPv5cPl.VteP3UYyK',
        address='456 Elm St',
        zipcode='23456',
        city='Othertown',
        country='Otherland',
        seller=True
    ),
    md.User(
        id=3,
        firstname='Anna',
        lastname='Bianchi',
        email='anna.bianchi@email.com',
        birthdate='03031990',
        pwhash='$2b$12$d1PTgoG9EUpebdrArF.v0eORHDq8yEyNgXSJbPv5cPl.VteP3UYyK',
        address='789 Oak St',
        zipcode='34567',
        city='Sometown',
        country='Someland',
        seller=True
    ),
    md.User(
        id=4,
        firstname='Giulia',
        lastname='Neri',
        email='giulia.neri@email.com',
        birthdate='04041990',
        pwhash='$2b$12$d1PTgoG9EUpebdrArF.v0eORHDq8yEyNgXSJbPv5cPl.VteP3UYyK',
        address='101 Pine St',
        zipcode='45678',
        city='Anycity',
        country='Anyland',
        seller=True
    ),
    md.User(
        id=5,
        firstname='Marco',
        lastname='Gialli',
        email='marco.gialli@email.com',
        birthdate='05051990',
        pwhash='$2b$12$d1PTgoG9EUpebdrArF.v0eORHDq8yEyNgXSJbPv5cPl.VteP3UYyK',
        address='202 Maple St',
        zipcode='56789',
        city='Yourtown',
        country='Yourland'
    ),
    md.User(
        id=6,
        firstname='Sara',
        lastname='Blu',
        email='sara.blu@email.com',
        birthdate='06061990',
        pwhash='$2b$12$d1PTgoG9EUpebdrArF.v0eORHDq8yEyNgXSJbPv5cPl.VteP3UYyK',
        address='303 Birch St',
        zipcode='67890',
        city='Hometown',
        country='Homeland'
    ),
    md.User(
        id=7,
        firstname='Francesco',
        lastname='Grigi',
        email='francesco.grigi@email.com',
        birthdate='07071990',
        pwhash='$2b$12$d1PTgoG9EUpebdrArF.v0eORHDq8yEyNgXSJbPv5cPl.VteP3UYyK',
        address='404 Cedar St',
        zipcode='78901',
        city='Newtown',
        country='Newland'
    ),
    md.User(
        id=8,
        firstname='Elena',
        lastname='Rossi',
        email='elena.rossi@email.com',
        birthdate='08081990',
        pwhash='$2b$12$d1PTgoG9EUpebdrArF.v0eORHDq8yEyNgXSJbPv5cPl.VteP3UYyK',
        address='505 Spruce St',
        zipcode='89012',
        city='Oldtown',
        country='Oldland'
    ),
    md.User(
        id=9,
        firstname='Simone',
        lastname='Verdi',
        email='simone.verdi@email.com',
        birthdate='09091990',
        pwhash='$2b$12$d1PTgoG9EUpebdrArF.v0eORHDq8yEyNgXSJbPv5cPl.VteP3UYyK',
        address='606 Fir St',
        zipcode='90123',
        city='Easttown',
        country='Eastland'
    ),
    md.User(
        id=10,
        firstname='Laura',
        lastname='Bianchi',
        email='laura.bianchi@email.com',
        birthdate='10101990',
        pwhash='$2b$12$d1PTgoG9EUpebdrArF.v0eORHDq8yEyNgXSJbPv5cPl.VteP3UYyK',
        address='707 Willow St',
        zipcode='01234',
        city='Westtown',
        country='Westland'
    ),
    md.User(
        id=11,
        firstname='Mario',
        lastname='Rossi',
        email='mario.rossi@email.com',
        birthdate='01011990',
        pwhash='$2b$12$d1PTgoG9EUpebdrArF.v0eORHDq8yEyNgXSJbPv5cPl.VteP3UYyK',
        address='606 Fir St',
        zipcode='90123',
        city='Easttown',
        country='Eastland'
    ),
    md.User(
        id=12,
        firstname='Gianni',
        lastname='Grigio',
        email='gianni.grigio@email.com',
        birthdate='01011945',
        pwhash='$2b$12$d1PTgoG9EUpebdrArF.v0eORHDq8yEyNgXSJbPv5cPl.VteP3UYyK',
        address='707 Willow St',
        zipcode='01234',
        city='Westtown',
        country='Westland'
    )
]

products = [
    # Interior items
    md.Product(
        id=1,
        name='IKEA KALLAX Shelf Unit',
        description='Versatile shelf unit for storage and display',
        brand='IKEA',
        fk_category=1,
        price=79.99,
        availability=100,
        fk_seller=2,
        imgpath='images/001.png'
    ),
    md.Product(
        id=2,
        name='Philips Hue White and Color Ambiance A19 LED Smart Bulb',
        description='Smart LED bulb with adjustable colors',
        brand='Philips',
        fk_category=1,
        price=49.99,
        availability=200,
        fk_seller=2,
        imgpath='images/002.png'
    ),
    md.Product(
        id=3,
        name='West Elm Mid-Century Nightstand',
        description='Stylish nightstand with a mid-century design',
        brand='West Elm',
        fk_category=1,
        price=299.00,
        availability=30,
        fk_seller=2,
        imgpath='images/003.png'
    ),
    md.Product(
        id=4,
        name='Nespresso VertuoPlus Coffee and Espresso Maker',
        description='Coffee maker with a variety of brewing options',
        brand='Nespresso',
        fk_category=1,
        price=149.99,
        availability=75,
        fk_seller=2,
        imgpath='images/004.png'
    ),
    md.Product(
        id=5,
        name='Dyson V11 Torque Drive Cordless Vacuum Cleaner',
        description='Powerful cordless vacuum with intelligent cleaning',
        brand='Dyson',
        fk_category=1,
        price=599.99,
        availability=40,
        fk_seller=2,
        imgpath='images/005.png'
    ),
    md.Product(
        id=6,
        name='Faux Fur Throw Blanket',
        description='Soft and cozy throw blanket for home decor',
        brand='Chic Home',
        fk_category=1,
        price=39.99,
        availability=150,
        fk_seller=2,
        imgpath='images/006.png'
    ),
    md.Product(
        id=7,
        name='Bose SoundLink Revolve+ Bluetooth Speaker',
        description='Portable Bluetooth speaker with 360-degree sound',
        brand='Bose',
        fk_category=1,
        price=329.00,
        availability=60,
        fk_seller=2,
        imgpath='images/007.png'
    ),
    md.Product(
        id=8,
        name='Zinus Green Tea Memory Foam Mattress',
        description='Comfortable memory foam mattress with green tea infusion',
        brand='Zinus',
        fk_category=1,
        price=299.00,
        availability=80,
        fk_seller=2,
        imgpath='images/008.png'
    ),
    md.Product(
        id=9,
        name='Amazon Echo Dot (4th Gen)',
        description='Smart speaker with Alexa voice control',
        brand='Amazon',
        fk_category=1,
        price=49.99,
        availability=200,
        fk_seller=2,
        imgpath='images/009.png'
    ),
    md.Product(
        id=10,
        name='Room Essentials 3-Drawer Storage Cart',
        description='Functional storage cart for organizing items',
        brand='Room Essentials',
        fk_category=1,
        price=39.99,
        availability=120,
        fk_seller=2,
        imgpath='images/010.png'
    ),

    # Sport and travel
    md.Product(
        id=11,
        name='The North Face Borealis Backpack',
        description='Durable backpack for travel and outdoor activities',
        brand='The North Face',
        fk_category=2,
        price=89.00,
        availability=100,
        fk_seller=3,
        imgpath='images/011.png'
    ),
    md.Product(
        id=12,
        name='Adidas Ultraboost 21 Running Shoes',
        description='High-performance running shoes with Boost cushioning',
        brand='Adidas',
        fk_category=2,
        price=179.99,
        availability=50,
        fk_seller=3,
        imgpath='images/012.png'
    ),
    md.Product(
        id=13,
        name='Osprey Atmos AG Backpack',
        description='Comfortable backpack with Anti-Gravity suspension',
        brand='Osprey',
        fk_category=2,
        price=399.95,
        availability=30,
        fk_seller=3,
        imgpath='images/013.png'
    ),
    md.Product(
        id=14,
        name='Fitbit Charge 5 Fitness Tracker',
        description='Advanced fitness tracker with health metrics',
        brand='Fitbit',
        fk_category=2,
        price=149.95,
        availability=80,
        fk_seller=3,
        imgpath='images/014.png'
    ),
    md.Product(
        id=15,
        name='Coleman Sundome Tent',
        description='Easy-to-set-up tent for camping',
        brand='Coleman',
        fk_category=2,
        price=99.99,
        availability=60,
        fk_seller=3,
        imgpath='images/015.png'
    ),
    md.Product(
        id=16,
        name='Under Armour Tech 2.0 Short Sleeve T-Shirt',
        description='Lightweight and breathable workout t-shirt',
        brand='Under Armour',
        fk_category=2,
        price=24.99,
        availability=150,
        fk_seller=3,
        imgpath='images/016.png'
    ),
    md.Product(
        id=17,
        name='YETI Rambler 20 oz Tumbler',
        description='Durable tumbler for hot and cold beverages',
        brand='YETI',
        fk_category=2,
        price=29.99,
        availability=200,
        fk_seller=3,
        imgpath='images/017.png'
    ),
    md.Product(
        id=18,
        name='Garmin Forerunner 245 GPS Running Watch',
        description='GPS running watch with advanced training features',
        brand='Garmin',
        fk_category=2,
        price=349.99,
        availability=40,
        fk_seller=3,
        imgpath='images/018.png'
    ),
    md.Product(
        id=19,
        name='REI Co-op Flash Pack 18',
        description='Lightweight daypack for hiking and travel',
        brand='REI',
        fk_category=2,
        price=59.95,
        availability=70,
        fk_seller=3,
        imgpath='images/019.png'
    ),
    md.Product(
        id=20,
        name='Nike Air Max 270 Sneakers',
        description='Stylish sneakers with a comfortable fit',
        brand='Nike',
        fk_category=2,
        price=149.99,
        availability=90,
        fk_seller=3,
        imgpath='images/020.png'
    ),

    # Jewellery
    md.Product(
        id=21,
        name='Tiffany & Co. Return to Tiffany Heart Tag Pendant',
        description='Iconic heart tag pendant in sterling silver',
        brand='Tiffany & Co.',
        fk_category=3,
        price=250.00,
        availability=20,
        fk_seller=4,
        imgpath='images/021.png'
    ),
    md.Product(
        id=22,
        name='Pandora Moments Snake Chain Bracelet',
        description='Classic snake chain bracelet for charms',
        brand='Pandora',
        fk_category=3,
        price=65.00,
        availability=100,
        fk_seller=4,
        imgpath='images/022.png'
    ),
    md.Product(
        id=23,
        name='Swarovski Crystal Heart Necklace',
        description='Elegant necklace with a heart-shaped crystal',
        brand='Swarovski',
        fk_category=3,
        price=79.00,
        availability=50,
        fk_seller=4,
        imgpath='images/023.png'
    ),
    md.Product(
        id=24,
        name='Cartier Love Bracelet',
        description='Iconic bracelet in 18K gold',
        brand='Cartier',
        fk_category=3,
        price=6000.00,
        availability=10,
        fk_seller=4,
        imgpath='images/024.png'
    ),
    md.Product(
        id=25,
        name='Michael Kors Parker Chronograph Watch',
        description='Stylish watch with a chronograph function',
        brand='Michael Kors',
        fk_category=3,
        price=250.00,
        availability=30,
        fk_seller=4,
        imgpath='images/025.png'
    ),
    md.Product(
        id=26,
        name='Chopard Happy Diamonds Pendant',
        description='Luxury pendant with moving diamonds',
        brand='Chopard',
        fk_category=3,
        price=1500.00,
        availability=15,
        fk_seller=4,
        imgpath='images/026.png'
    ),
    md.Product(
        id=27,
        name='Bulgari B.Zero1 Ring',
        description='Iconic ring in 18K gold and ceramic',
        brand='Bulgari',
        fk_category=3,
        price=1200.00,
        availability=5,
        fk_seller=4,
        imgpath='images/027.png'
    ),
    md.Product(
        id=28,
        name='David Yurman Cable Classic Bracelet',
        description='Signature bracelet in sterling silver',
        brand='David Yurman',
        fk_category=3,
        price=450.00,
        availability=25,
        fk_seller=4,
        imgpath='images/028.png'
    ),
    md.Product(
        id=29,
        name='Van Cleef & Arpels Alhambra Necklace',
        description='Iconic necklace with clover motifs',
        brand='Van Cleef & Arpels',
        fk_category=3,
        price=3000.00,
        availability=8,
        fk_seller=4,
        imgpath='images/029.png'
    ),
    md.Product(
        id=30,
        name='Tiffany & Co. Elsa Peretti Open Heart Pendant',
        description='Elegant open heart pendant in sterling silver',
        brand='Tiffany & Co.',
        fk_category=3,
        price=200.00,
        availability=12,
        fk_seller=4,
        imgpath='images/030.png'
    ),

    # Accessories
    md.Product(
        id=31,
        name='Ray-Ban Wayfarer Sunglasses',
        description='Classic sunglasses with UV protection',
        brand='Ray-Ban',
        fk_category=4,
        price=150.00,
        availability=80,
        fk_seller=1,
        imgpath='images/031.png'
    ),
    md.Product(
        id=32,
        name='Fjällräven Kånken Backpack',
        description='Iconic backpack for everyday use',
        brand='Fjällräven',
        fk_category=4,
        price=80.00,
        availability=100,
        fk_seller=1,
        imgpath='images/032.png'
    ),
    md.Product(
        id=33,
        name='Montblanc Meisterstück Rollerball Pen',
        description='Luxury rollerball pen for writing',
        brand='Montblanc',
        fk_category=4,
        price=300.00,
        availability=20,
        fk_seller=1,
        imgpath='images/033.png'
    ),
    md.Product(
        id=34,
        name='Herschel Little America Backpack',
        description='Stylish backpack with a vintage look',
        brand='Herschel',
        fk_category=4,
        price=109.99,
        availability=50,
        fk_seller=1,
        imgpath='images/034.png'
    ),
    md.Product(
        id=35,
        name='Tumi Alpha 3 Expandable International 4-Wheeled Carry-On',
        description='Durable carry-on luggage with expansion capability',
        brand='Tumi',
        fk_category=4,
        price=595.00,
        availability=15,
        fk_seller=1,
        imgpath='images/035.png'
    ),
    md.Product(
        id=36,
        name='Patagonia Black Hole Duffel Bag',
        description='Versatile duffel bag for travel and outdoor use',
        brand='Patagonia',
        fk_category=4,
        price=149.00,
        availability=40,
        fk_seller=1,
        imgpath='images/036.png'
    ),
    md.Product(
        id=37,
        name='Kate Spade New York Cameron Street Lacey Wallet',
        description='Stylish wallet with multiple card slots',
        brand='Kate Spade',
        fk_category=4,
        price=158.00,
        availability=25,
        fk_seller=1,
        imgpath='images/037.png'
    ),
    md.Product(
        id=38,
        name='North Face Base Camp Duffel Bag',
        description='Durable duffel bag for travel and adventure',
        brand='The North Face',
        fk_category=4,
        price=130.00,
        availability=60,
        fk_seller=1,
        imgpath='images/038.png'
    ),
    md.Product(
        id=39,
        name='Lululemon Everywhere Belt Bag',
        description='Compact belt bag for essentials',
        brand='Lululemon',
        fk_category=4,
        price=38.00,
        availability=150,
        fk_seller=1,
        imgpath='images/039.png'
    ),
    md.Product(
        id=40,
        name='Gucci GG Marmont Matelassé Mini Bag',
        description='Luxury mini bag with iconic GG logo',
        brand='Gucci',
        fk_category=4,
        price=980.00,
        availability=10,
        fk_seller=1,
        imgpath='images/040.png'
    ),

    # Automobiles
    md.Product(
        id=41,
        name='Tesla Model 3',
        description='Electric sedan with advanced technology',
        brand='Tesla',
        fk_category=5,
        price=39990.00,
        availability=5,
        fk_seller=1,
        imgpath='images/041.png'
    ),
    md.Product(
        id=42,
        name='Ford F-150',
        description='Popular pickup truck with powerful performance',
        brand='Ford',
        fk_category=5,
        price=29995.00,
        availability=10,
        fk_seller=1,
        imgpath='images/042.png'
    ),
    md.Product(
        id=43,
        name='Honda Accord',
        description='Reliable midsize sedan with great fuel efficiency',
        brand='Honda',
        fk_category=5,
        price=24970.00,
        availability=15,
        fk_seller=1,
        imgpath='images/043.png'
    ),
    md.Product(
        id=44,
        name='Chevrolet Silverado 1500',
        description='Durable pickup truck with advanced features',
        brand='Chevrolet',
        fk_category=5,
        price=35000.00,
        availability=8,
        fk_seller=1,
        imgpath='images/044.png'
    ),
    md.Product(
        id=45,
        name='BMW 3 Series',
        description='Luxury sedan with sporty performance',
        brand='BMW',
        fk_category=5,
        price=41200.00,
        availability=12,
        fk_seller=1,
        imgpath='images/045.png'
    ),
    md.Product(
        id=46,
        name='Toyota Camry',
        description='Midsize sedan with a reputation for reliability',
        brand='Toyota',
        fk_category=5,
        price=24425.00,
        availability=20,
        fk_seller=1,
        imgpath='images/046.png'
    ),
    md.Product(
        id=47,
        name='Mercedes-Benz C-Class',
        description='Luxury sedan with advanced technology',
        brand='Mercedes-Benz',
        fk_category=5,
        price=41900.00,
        availability=7,
        fk_seller=1,
        imgpath='images/047.png'
    ),
    md.Product(
        id=48,
        name='Nissan Rogue',
        description='Compact SUV with spacious interior',
        brand='Nissan',
        fk_category=5,
        price=26990.00,
        availability=18,
        fk_seller=1,
        imgpath='images/048.png'
    ),
    md.Product(
        id=49,
        name='Subaru Outback',
        description='Versatile wagon with all-wheel drive',
        brand='Subaru',
        fk_category=5,
        price=26895.00,
        availability=14,
        fk_seller=1,
        imgpath='images/049.png'
    ),
    md.Product(
        id=50,
        name='Volkswagen Golf',
        description='Compact hatchback with fun driving dynamics',
        brand='Volkswagen',
        fk_category=5,
        price=23000.00,
        availability=25,
        fk_seller=1,
        imgpath='images/050.png'
    ),

    # House
    md.Product(
        id=51,
        name='Samsung 65-Inch QLED 4K Smart TV',
        description='Stunning 4K resolution with vibrant colors',
        brand='Samsung',
        fk_category=6,
        price=1499.99,
        availability=10,
        fk_seller=1,
        imgpath='images/051.png'
    ),
    md.Product(
        id=52,
        name='Dyson Pure Cool Link Air Purifier',
        description='Air purifier with Wi-Fi connectivity',
        brand='Dyson',
        fk_category=6,
        price=499.99,
        availability=15,
        fk_seller=1,
        imgpath='images/052.png'
    ),
    md.Product(
        id=53,
        name='Instant Pot Duo 7-in-1 Electric Pressure Cooker',
        description='Versatile kitchen appliance for quick meals',
        brand='Instant Pot',
        fk_category=6,
        price=89.99,
        availability=100,
        fk_seller=1,
        imgpath='images/053.png'
    ),
    md.Product(
        id=54,
        name='KitchenAid Artisan Stand Mixer',
        description='Iconic stand mixer for baking and cooking',
        brand='KitchenAid',
        fk_category=6,
        price=379.99,
        availability=20,
        fk_seller=1,
        imgpath='images/054.png'
    ),
    md.Product(
        id=55,
        name='iRobot Roomba 675 Robot Vacuum',
        description='Smart robot vacuum with Wi-Fi connectivity',
        brand='iRobot',
        fk_category=6,
        price=299.99,
        availability=30,
        fk_seller=1,
        imgpath='images/055.png'
    ),
    md.Product(
        id=56,
        name='Cuisinart 14-Cup Food Processor',
        description='Powerful food processor for meal prep',
        brand='Cuisinart',
        fk_category=6,
        price=199.99,
        availability=25,
        fk_seller=1,
        imgpath='images/056.png'
    ),
    md.Product(
        id=57,
        name='Nespresso Essenza Mini Coffee Machine',
        description='Compact coffee machine for espresso lovers',
        brand='Nespresso',
        fk_category=6,
        price=89.99,
        availability=50,
        fk_seller=1,
        imgpath='images/057.png'
    ),
    md.Product(
        id=58,
        name='Breville Smart Oven Air Fryer',
        description='Versatile oven with air frying capabilities',
        brand='Breville',
        fk_category=6,
        price=299.95,
        availability=15,
        fk_seller=1,
        imgpath='images/058.png'
    ),
    md.Product(
        id=59,
        name='Philips Airfryer XXL',
        description='Healthy air fryer for crispy meals',
        brand='Philips',
        fk_category=6,
        price=299.99,
        availability=20,
        fk_seller=1,
        imgpath='images/059.png'
    ),
    md.Product(
        id=60,
        name='Lodge Cast Iron Skillet',
        description='Durable cast iron skillet for cooking',
        brand='Lodge',
        fk_category=6,
        price=29.99,
        availability=150,
        fk_seller=1,
        imgpath='images/060.png'
    ),

    # Music
    md.Product(
        id=61,
        name='Yamaha P-125 Digital Piano',
        description='Compact digital piano with weighted keys',
        brand='Yamaha',
        fk_category=7,
        price=649.99,
        availability=20,
        fk_seller=1,
        imgpath='images/061.png'
    ),
    md.Product(
        id=62,
        name='Bose QuietComfort 35 II Wireless Headphones',
        description='Noise-canceling headphones with great sound',
        brand='Bose',
        fk_category=7,
        price=299.00,
        availability=30,
        fk_seller=1,
        imgpath='images/062.png'
    ),
    md.Product(
        id=63,
        name='Gibson Les Paul Standard Electric Guitar',
        description='Iconic electric guitar with a classic sound',
        brand='Gibson',
        fk_category=7,
        price=2499.00,
        availability=10,
        fk_seller=1,
        imgpath='images/063.png'
    ),
    md.Product(
        id=64,
        name='Fender American Professional II Stratocaster',
        description='High-quality electric guitar with versatile tones',
        brand='Fender',
        fk_category=7,
        price=1499.99,
        availability=15,
        fk_seller=1,
        imgpath='images/064.png'
    ),
    md.Product(
        id=65,
        name='Korg Volca FM Synthesizer',
        description='Compact FM synthesizer for music production',
        brand='Korg',
        fk_category=7,
        price=149.00,
        availability=50,
        fk_seller=1,
        imgpath='images/065.png'
    ),
    md.Product(
        id=66,
        name='Roland TD-1K Electronic Drum Kit',
        description='Compact electronic drum kit for practice',
        brand='Roland',
        fk_category=7,
        price=499.99,
        availability=20,
        fk_seller=1,
        imgpath='images/066.png'
    ),
    md.Product(
        id=67,
        name='Shure SM58 Vocal Microphone',
        description='Legendary vocal microphone for live performance',
        brand='Shure',
        fk_category=7,
        price=99.00,
        availability=100,
        fk_seller=1,
        imgpath='images/067.png'
    ),
    md.Product(
        id=68,
        name='Native Instruments Komplete 13',
        description='Comprehensive music production software suite',
        brand='Native Instruments',
        fk_category=7,
        price=599.00,
        availability=15,
        fk_seller=1,
        imgpath='images/068.png'
    ),
    md.Product(
        id=69,
        name='Audio-Technica AT2020 Condenser Microphone',
        description='High-quality condenser microphone for recording',
        brand='Audio-Technica',
        fk_category=7,
        price=99.00,
        availability=50,
        fk_seller=1,
        imgpath='images/069.png'
    ),
    md.Product(
        id=70,
        name='IK Multimedia iRig Keys 37',
        description='Portable MIDI keyboard for music production',
        brand='IK Multimedia',
        fk_category=7,
        price=99.99,
        availability=40,
        fk_seller=1,
        imgpath='images/070.png'
    ),

    # Books
    md.Product(
        id=71,
        name='The Great Gatsby by F. Scott Fitzgerald',
        description='Classic novel set in the Jazz Age',
        brand='Scribner',
        fk_category=8,
        price=10.99,
        availability=200,
        fk_seller=1,
        imgpath='images/071.png'
    ),
    md.Product(
        id=72,
        name='To Kill a Mockingbird by Harper Lee',
        description='Pulitzer Prize-winning novel about racial injustice',
        brand='HarperCollins',
        fk_category=8,
        price=7.99,
        availability=150,
        fk_seller=1,
        imgpath='images/072.png'
    ),
    md.Product(
        id=73,
        name='1984 by George Orwell',
        description='Dystopian novel about totalitarianism',
        brand='Harcourt',
        fk_category=8,
        price=9.99,
        availability=180,
        fk_seller=1,
        imgpath='images/073.png'
    ),
    md.Product(
        id=74,
        name='Pride and Prejudice by Jane Austen',
        description='Classic novel about love and social class',
        brand='Penguin Classics',
        fk_category=8,
        price=12.00,
        availability=120,
        fk_seller=1,
        imgpath='images/074.png'
    ),
    md.Product(
        id=75,
        name='The Catcher in the Rye by J.D. Salinger',
        description='Novel about teenage angst and alienation',
        brand='Little, Brown and Company',
        fk_category=8,
        price=10.99,
        availability=100,
        fk_seller=1,
        imgpath='images/075.png'
    ),
    md.Product(
        id=76,
        name='The Alchemist by Paulo Coelho',
        description='Philosophical novel about following your dreams',
        brand='HarperOne',
        fk_category=8,
        price=16.00,
        availability=80,
        fk_seller=1,
        imgpath='images/076.png'
    ),
    md.Product(
        id=77,
        name='The Hobbit by J.R.R. Tolkien',
        description='Fantasy novel about a hobbit’s adventure',
        brand='Houghton Mifflin Harcourt',
        fk_category=8,
        price=14.99,
        availability=90,
        fk_seller=1,
        imgpath='images/077.png'
    ),
    md.Product(
        id=78,
        name='The Da Vinci Code by Dan Brown',
        description='Thriller novel about art, history, and religion',
        brand='Doubleday',
        fk_category=8,
        price=19.99,
        availability=70,
        fk_seller=1,
        imgpath='images/078.png'
    ),
    md.Product(
        id=79,
        name='The Silent Patient by Alex Michaelides',
        description='Psychological thriller about a woman’s silence',
        brand='Celadon Books',
        fk_category=8,
        price=16.99,
        availability=60,
        fk_seller=1,
        imgpath='images/079.png'
    ),
    md.Product(
        id=80,
        name='Becoming by Michelle Obama',
        description='Memoir by the former First Lady of the United States',
        brand='Crown Publishing Group',
        fk_category=8,
        price=24.99,
        availability=50,
        fk_seller=1,
        imgpath='images/080.png'
    ),

    # Kids
    md.Product(
        id=81,
        name='LEGO Classic Medium Creative Brick Box',
        description='Versatile LEGO set for creative building',
        brand='LEGO',
        fk_category=9,
        price=49.99,
        availability=100,
        fk_seller=1,
        imgpath='images/081.png'
    ),
    md.Product(
        id=82,
        name='Barbie Dreamhouse Dollhouse',
        description='Large dollhouse with furniture and accessories',
        brand='Barbie',
        fk_category=9,
        price=199.99,
        availability=30,
        fk_seller=1,
        imgpath='images/082.png'
    ),
    md.Product(
        id=83,
        name='Fisher-Price Laugh & Learn Smart Stages Chair',
        description='Interactive chair that teaches and entertains',
        brand='Fisher-Price',
        fk_category=9,
        price=79.99,
        availability=50,
        fk_seller=1,
        imgpath='images/083.png'
    ),
    md.Product(
        id=84,
        name='Melissa & Doug Wooden Building Blocks',
        description='Classic wooden blocks for creative play',
        brand='Melissa & Doug',
        fk_category=9,
        price=29.99,
        availability=150,
        fk_seller=1,
        imgpath='images/084.png'
    ),
    md.Product(
        id=85,
        name='Hot Wheels 20-Car Pack',
        description='Pack of 20 die-cast cars for racing fun',
        brand='Hot Wheels',
        fk_category=9,
        price=29.99,
        availability=80,
        fk_seller=1,
        imgpath='images/085.png'
    ),
    md.Product(
        id=86,
        name='Play-Doh 36-Can Mega Pack',
        description='Large pack of colorful modeling compound',
        brand='Play-Doh',
        fk_category=9,
        price=49.99,
        availability=60,
        fk_seller=1,
        imgpath='images/086.png'
    ),
    md.Product(
        id=87,
        name='Nerf N-Strike Elite Disruptor',
        description='Blaster with rotating drum for foam darts',
        brand='Nerf',
        fk_category=9,
        price=19.99,
        availability=200,
        fk_seller=1,
        imgpath='images/087.png'
    ),
    md.Product(
        id=88,
        name='VTech Sit-to-Stand Learning Walker',
        description='Interactive walker that grows with your child',
        brand='VTech',
        fk_category=9,
        price=49.99,
        availability=100,
        fk_seller=1,
        imgpath='images/088.png'
    ),
    md.Product(
        id=89,
        name='Crayola Inspiration Art Case',
        description='Complete art set for creative kids',
        brand='Crayola',
        fk_category=9,
        price=29.99,
        availability=150,
        fk_seller=1,
        imgpath='images/089.png'
    ),
    md.Product(
        id=90,
        name='Disney Princess Dress-Up Trunk',
        description='Costume trunk with dresses and accessories',
        brand='Disney',
        fk_category=9,
        price=49.99,
        availability=40,
        fk_seller=1,
        imgpath='images/090.png'
    ),

    # Pets
    md.Product(
        id=91,
        name='PetSafe ScoopFree Ultra Self-Cleaning Litter Box',
        description='Automatic litter box with a self-cleaning feature',
        brand='PetSafe',
        fk_category=10,
        price=149.95,
        availability=20,
        fk_seller=1,
        imgpath='images/091.png'
    ),
    md.Product(
        id=92,
        name='KONG Classic Dog Toy',
        description='Durable rubber toy for dogs',
        brand='KONG',
        fk_category=10,
        price=12.99,
        availability=100,
        fk_seller=1,
        imgpath='images/092.png'
    ),
    md.Product(
        id=93,
        name='Frisco Heavy Duty Dog Crate',
        description='Sturdy dog crate for training and travel',
        brand='Frisco',
        fk_category=10,
        price=89.99,
        availability=50,
        fk_seller=1,
        imgpath='images/093.png'
    ),
    md.Product(
        id=94,
        name='Hill’s Science Diet Adult Dry Dog Food',
        description='Nutritious dry food for adult dogs',
        brand='Hill’s Science Diet',
        fk_category=10,
        price=54.99,
        availability=30,
        fk_seller=1,
        imgpath='images/094.png'
    ),
    md.Product(
        id=95,
        name='PetFusion Ultimate Dog Bed',
        description='Orthopedic dog bed for comfort',
        brand='PetFusion',
        fk_category=10,
        price=99.95,
        availability=25,
        fk_seller=1,
        imgpath='images/095.png'
    ),
    md.Product(
        id=96,
        name='Catit Senses 2.0 Food Tree',
        description='Interactive feeder for cats',
        brand='Catit',
        fk_category=10,
        price=29.99,
        availability=60,
        fk_seller=1,
        imgpath='images/096.png'
    ),
    md.Product(
        id=97,
        name='Tidy Cats Breeze Cat Litter System',
        description='Litter system with odor control',
        brand='Tidy Cats',
        fk_category=10,
        price=39.99,
        availability=40,
        fk_seller=1,
        imgpath='images/097.png'
    ),
    md.Product(
        id=98,
        name='Outward Hound Hide-A-Squirrel Puzzle Toy',
        description='Interactive puzzle toy for dogs',
        brand='Outward Hound',
        fk_category=10,
        price=19.99,
        availability=80,
        fk_seller=1,
        imgpath='images/098.png'
    ),
    md.Product(
        id=99,
        name='PetSafe Healthy Pet Gravity Feeder',
        description='Automatic feeder for pets',
        brand='PetSafe',
        fk_category=10,
        price=29.99,
        availability=100,
        fk_seller=1,
        imgpath='images/099.png'
    ),
    md.Product(
        id=100,
        name='Burt’s Bees for Pets Natural Shampoo',
        description='Natural shampoo for dogs and cats',
        brand='Burt’s Bees',
        fk_category=10,
        price=12.99,
        availability=150,
        fk_seller=1,
        imgpath='images/100.png'
    ),

    # Fashion
    md.Product(
        id=101,
        name='Levi’s 501 Original Fit Jeans',
        description='Classic straight-leg jeans for men',
        brand='Levi’s',
        fk_category=11,
        price=59.99,
        availability=100,
        fk_seller=1,
        imgpath='images/101.png'
    ),
    md.Product(
        id=102,
        name='Nike Air Force 1 Sneakers',
        description='Iconic sneakers with a classic design',
        brand='Nike',
        fk_category=11,
        price=90.00,
        availability=80,
        fk_seller=1,
        imgpath='images/102.png'
    ),
    md.Product(
        id=103,
        name='Adidas Originals Trefoil Hoodie',
        description='Comfortable hoodie with a classic logo',
        brand='Adidas',
        fk_category=11,
        price=65.00,
        availability=150,
        fk_seller=1,
        imgpath='images/103.png'
    ),
    md.Product(
        id=104,
        name='H&M Basic T-Shirt',
        description='Essential t-shirt for everyday wear',
        brand='H&M',
        fk_category=11,
        price=14.99,
        availability=200,
        fk_seller=1,
        imgpath='images/104.png'
    ),
    md.Product(
        id=105,
        name='Zara Faux Leather Biker Jacket',
        description='Stylish biker jacket for a trendy look',
        brand='Zara',
        fk_category=11,
        price=89.90,
        availability=50,
        fk_seller=1,
        imgpath='images/105.png'
    ),
    md.Product(
        id=106,
        name='Calvin Klein Modern Cotton Bralette',
        description='Comfortable bralette for everyday wear',
        brand='Calvin Klein',
        fk_category=11,
        price=29.50,
        availability=100,
        fk_seller=1,
        imgpath='images/106.png'
    ),
    md.Product(
        id=107,
        name='Tommy Hilfiger Iconic Logo Cap',
        description='Stylish cap with a logo design',
        brand='Tommy Hilfiger',
        fk_category=11,
        price=35.00,
        availability=80,
        fk_seller=1,
        imgpath='images/107.png'
    ),
    md.Product(
        id=108,
        name='Puma Suede Classic Sneakers',
        description='Timeless sneakers with a suede upper',
        brand='Puma',
        fk_category=11,
        price=70.00,
        availability=60,
        fk_seller=1,
        imgpath='images/108.png'
    ),
    md.Product(
        id=109,
        name='Uniqlo Ultra Light Down Jacket',
        description='Lightweight down jacket for warmth',
        brand='Uniqlo',
        fk_category=11,
        price=99.90,
        availability=40,
        fk_seller=1,
        imgpath='images/109.png'
    ),
    md.Product(
        id=110,
        name='Chanel Classic Flap Bag',
        description='Iconic handbag with a timeless design',
        brand='Chanel',
        fk_category=11,
        price=5500.00,
        availability=5,
        fk_seller=1,
        imgpath='images/110.png'
    ),

    # Computers
    md.Product(
        id=111,
        name='Apple MacBook Air (M1, 2020)',
        description='Lightweight laptop with M1 chip',
        brand='Apple',
        fk_category=12,
        price=999.00,
        availability=20,
        fk_seller=1,
        imgpath='images/111.png'
    ),
    md.Product(
        id=112,
        name='Dell XPS 13 (2021)',
        description='High-performance laptop with InfinityEdge display',
        brand='Dell',
        fk_category=12,
        price=1249.99,
        availability=15,
        fk_seller=1,
        imgpath='images/112.png'
    ),
    md.Product(
        id=113,
        name='HP Spectre x360 14',
        description='Convertible laptop with a stunning design',
        brand='HP',
        fk_category=12,
        price=1399.99,
        availability=10,
        fk_seller=1,
        imgpath='images/113.png'
    ),
    md.Product(
        id=114,
        name='Lenovo ThinkPad X1 Carbon Gen 9',
        description='Business laptop with a durable design',
        brand='Lenovo',
        fk_category=12,
        price=1499.99,
        availability=8,
        fk_seller=1,
        imgpath='images/114.png'
    ),
    md.Product(
        id=115,
        name='Asus ROG Zephyrus G14',
        description='Gaming laptop with powerful performance',
        brand='Asus',
        fk_category=12,
        price=1499.00,
        availability=12,
        fk_seller=1,
        imgpath='images/115.png'
    ),
    md.Product(
        id=116,
        name='Microsoft Surface Laptop 4',
        description='Sleek laptop with a high-resolution display',
        brand='Microsoft',
        fk_category=12,
        price=999.99,
        availability=15,
        fk_seller=1,
        imgpath='images/116.png'
    ),
    md.Product(
        id=117,
        name='Acer Aspire 5',
        description='Affordable laptop for everyday use',
        brand='Acer',
        fk_category=12,
        price=499.99,
        availability=25,
        fk_seller=1,
        imgpath='images/117.png'
    ),
    md.Product(
        id=118,
        name='Razer Blade 15',
        description='High-performance gaming laptop',
        brand='Razer',
        fk_category=12,
        price=1999.99,
        availability=5,
        fk_seller=1,
        imgpath='images/118.png'
    ),
    md.Product(
        id=119,
        name='Apple iMac 24-inch (M1, 2021)',
        description='All-in-one desktop with M1 chip',
        brand='Apple',
        fk_category=12,
        price=1299.00,
        availability=10,
        fk_seller=1,
        imgpath='images/119.png'
    ),
    md.Product(
        id=120,
        name='Samsung Galaxy Book Pro 360',
        description='2-in-1 laptop with AMOLED display',
        brand='Samsung',
        fk_category=12,
        price=1399.99,
        availability=8,
        fk_seller=1,
        imgpath='images/120.png'
    ),

    # Smartphones
    md.Product(
        id=121,
        name='Apple iPhone 13',
        description='Latest iPhone with A15 Bionic chip',
        brand='Apple',
        fk_category=13,
        price=799.00,
        availability=20,
        fk_seller=1,
        imgpath='images/121.png'
    ),
    md.Product(
        id=122,
        name='Samsung Galaxy S21',
        description='Flagship smartphone with a stunning display',
        brand='Samsung',
        fk_category=13,
        price=799.99,
        availability=15,
        fk_seller=1,
        imgpath='images/122.png'
    ),
    md.Product(
        id=123,
        name='Google Pixel 6',
        description='Smartphone with an excellent camera',
        brand='Google',
        fk_category=13,
        price=599.00,
        availability=25,
        fk_seller=1,
        imgpath='images/123.png'
    ),
    md.Product(
        id=124,
        name='OnePlus 9',
        description='High-performance smartphone with fast charging',
        brand='OnePlus',
        fk_category=13,
        price=729.00,
        availability=10,
        fk_seller=1,
        imgpath='images/124.png'
    ),
    md.Product(
        id=125,
        name='Xiaomi Mi 11',
        description='Flagship smartphone with a powerful camera',
        brand='Xiaomi',
        fk_category=13,
        price=749.00,
        availability=12,
        fk_seller=1,
        imgpath='images/125.png'
    ),
    md.Product(
        id=126,
        name='Sony Xperia 1 III',
        description='Premium smartphone with a 4K display',
        brand='Sony',
        fk_category=13,
        price=1299.00,
        availability=8,
        fk_seller=1,
        imgpath='images/126.png'
    ),
    md.Product(
        id=127,
        name='Oppo Find X3 Pro',
        description='High-end smartphone with a unique design',
        brand='Oppo',
        fk_category=13,
        price=1149.00,
        availability=5,
        fk_seller=1,
        imgpath='images/127.png'
    ),
    md.Product(
        id=128,
        name='Motorola Edge 20',
        description='Mid-range smartphone with a sleek design',
        brand='Motorola',
        fk_category=13,
        price=499.00,
        availability=20,
        fk_seller=1,
        imgpath='images/128.png'
    ),
    md.Product(
        id=129,
        name='Nokia G50',
        description='Affordable smartphone with 5G capability',
        brand='Nokia',
        fk_category=13,
        price=299.00,
        availability=30,
        fk_seller=1,
        imgpath='images/129.png'
    ),
    md.Product(
        id=130,
        name='Huawei P40 Pro',
        description='Flagship smartphone with advanced camera features',
        brand='Huawei',
        fk_category=13,
        price=999.00,
        availability=10,
        fk_seller=1,
        imgpath='images/130.png'
    ),

    # Movies
    md.Product(
        id=131,
        name='The Shawshank Redemption (Blu-ray)',
        description='Classic film about hope and friendship',
        brand='Columbia Pictures',
        fk_category=14,
        price=14.99,
        availability=100,
        fk_seller=1,
        imgpath='images/131.png'
    ),
    md.Product(
        id=132,
        name='Inception (Blu-ray)',
        description='Mind-bending thriller directed by Christopher Nolan',
        brand='Warner Bros.',
        fk_category=14,
        price=14.99,
        availability=80,
        fk_seller=1,
        imgpath='images/132.png'
    ),
    md.Product(
        id=133,
        name='The Godfather (Blu-ray)',
        description='Iconic film about a crime family',
        brand='Paramount Pictures',
        fk_category=14,
        price=14.99,
        availability=90,
        fk_seller=1,
        imgpath='images/133.png'
    ),
    md.Product(
        id=134,
        name='Pulp Fiction (Blu-ray)',
        description='Cult classic film directed by Quentin Tarantino',
        brand='Miramax',
        fk_category=14,
        price=14.99,
        availability=70,
        fk_seller=1,
        imgpath='images/134.png'
    ),
    md.Product(
        id=135,
        name='The Dark Knight (Blu-ray)',
        description='Superhero film featuring Batman and the Joker',
        brand='Warner Bros.',
        fk_category=14,
        price=14.99,
        availability=60,
        fk_seller=1,
        imgpath='images/135.png'
    ),
    md.Product(
        id=136,
        name='Forrest Gump (Blu-ray)',
        description='Heartwarming story of a man’s extraordinary life',
        brand='Paramount Pictures',
        fk_category=14,
        price=14.99,
        availability=50,
        fk_seller=1,
        imgpath='images/136.png'
    ),
    md.Product(
        id=137,
        name='The Matrix (Blu-ray)',
        description='Sci-fi film about a dystopian future',
        brand='Warner Bros.',
        fk_category=14,
        price=14.99,
        availability=40,
        fk_seller=1,
        imgpath='images/137.png'
    ),
    md.Product(
        id=138,
        name='Gladiator (Blu-ray)',
        description='Epic historical drama directed by Ridley Scott',
        brand='DreamWorks',
        fk_category=14,
        price=14.99,
        availability=30,
        fk_seller=1,
        imgpath='images/138.png'
    ),
    md.Product(
        id=139,
        name='The Silence of the Lambs (Blu-ray)',
        description='Thriller about a young FBI cadet and a cannibalistic serial killer',
        brand='Orion Pictures',
        fk_category=14,
        price=14.99,
        availability=20,
        fk_seller=1,
        imgpath='images/139.png'
    ),
    md.Product(
        id=140,
        name='The Lord of the Rings: The Fellowship of the Ring (Blu-ray)',
        description='Fantasy epic based on J.R.R. Tolkien’s novel',
        brand='New Line Cinema',
        fk_category=14,
        price=14.99,
        availability=10,
        fk_seller=1,
        imgpath='images/140.png'
    ),

    # Other items
    md.Product(
        id=141,
        name='Amazon Gift Card',
        description='Gift card for Amazon purchases',
        brand='Amazon',
        fk_category=15,
        price=50.00,
        availability=200,
        fk_seller=1,
        imgpath='images/141.png'
    ),
    md.Product(
        id=142,
        name='Fujifilm Instax Mini 11 Instant Camera',
        description='Instant camera for capturing memories',
        brand='Fujifilm',
        fk_category=15,
        price=69.95,
        availability=100,
        fk_seller=1,
        imgpath='images/142.png'
    ),
    md.Product(
        id=143,
        name='Jenga Classic Game',
        description='Classic stacking game for family fun',
        brand='Hasbro',
        fk_category=15,
        price=19.99,
        availability=150,
        fk_seller=1,
        imgpath='images/143.png'
    ),
    md.Product(
        id=144,
        name='Nintendo Switch Console',
        description='Popular gaming console for all ages',
        brand='Nintendo',
        fk_category=15,
        price=299.99,
        availability=50,
        fk_seller=1,
        imgpath='images/144.png'
    ),
    md.Product(
        id=145,
        name='Fitbit Inspire 2 Health and Fitness Tracker',
        description='Fitness tracker with heart rate monitoring',
        brand='Fitbit',
        fk_category=15,
        price=99.95,
        availability=80,
        fk_seller=1,
        imgpath='images/145.png'
    ),
    md.Product(
        id=146,
        name='LEGO Star Wars Millennium Falcon',
        description='Iconic LEGO set for Star Wars fans',
        brand='LEGO',
        fk_category=15,
        price=169.99,
        availability=30,
        fk_seller=1,
        imgpath='images/146.png'
    ),
    md.Product(
        id=147,
        name='Sony PlayStation 5 Console',
        description='Next-gen gaming console with powerful performance',
        brand='Sony',
        fk_category=15,
        price=499.99,
        availability=20,
        fk_seller=1,
        imgpath='images/147.png'
    ),
    md.Product(
        id=148,
        name='Apple AirPods Pro',
        description='Wireless earbuds with active noise cancellation',
        brand='Apple',
        fk_category=15,
        price=249.00,
        availability=40,
        fk_seller=1,
        imgpath='images/148.png'
    ),
    md.Product(
        id=149,
        name='Kindle Paperwhite',
        description='E-reader with a high-resolution display',
        brand='Amazon',
        fk_category=15,
        price=139.99,
        availability=60,
        fk_seller=1,
        imgpath='images/149.png'
    ),
    md.Product(
        id=150,
        name='Oculus Quest 2 VR Headset',
        description='All-in-one VR headset for immersive experiences',
        brand='Oculus',
        fk_category=15,
        price=299.00,
        availability=15,
        fk_seller=1,
        imgpath='images/150.png'
    )
]


# -----------------------------------------------------------------------------------


def insert():
    db.add_list(categories)
    db.add_list(statuses)
    db.add_list(users)
    db.add_list(products)

    n_users = 12
    n_products = 150

    for n in range(8):  # 8 orders for each user
        # CARTS
        carts = []
        for user_id in range(5, n_users + 1):   # user id between 5 and 12
            selected_products = random.sample(range(1, n_products + 1), 5)  # 5 casual product ID
            for product_id in selected_products:
                quantity = random.randint(1, 3)  # Casual qt. between 1 and 3
                carts.append(
                        md.Cart(
                            fk_user=user_id,
                            fk_product=product_id,
                            quantity=quantity
                        )
                    )

        db.add_list(carts)

        # ORDERS
        orders = []
        for user in users[4:]:   # from User n.4 (the first 4 users are Sellers)
            orders.append(
                md.Order(
                    fk_user=user.id,
                    fk_status=random.randint(1, 7),  # Status ID between 1 and 7
                    date='20240901',
                    address=user.address,
                    zipcode=user.zipcode,
                    city=user.city,
                    country=user.country
                )
            )

        db.add_list(orders)

    return "Data inserted"
