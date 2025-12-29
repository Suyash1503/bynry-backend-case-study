from decimal import Decimal
from sqlalchemy.exc import IntegrityError

@app.route('/api/products', methods=['POST'])
def create_product():
    data = request.json

    try:
        if not data.get('name') or not data.get('sku'):
            return {"error": "Product name and SKU are required"}, 400

        existing_product = Product.query.filter_by(sku=data['sku']).first()
        if existing_product:
            return {"error": "SKU already exists"}, 409

        product = Product(
            name=data['name'],
            sku=data['sku'],
            price=Decimal(str(data.get('price', 0)))
        )

        db.session.add(product)
        db.session.flush()

        if data.get('warehouse_id'):
            inventory = Inventory(
                product_id=product.id,
                warehouse_id=data['warehouse_id'],
                quantity=data.get('initial_quantity', 0)
            )
            db.session.add(inventory)

        db.session.commit()

        return {"message": "Product created successfully", "product_id": product.id}, 201

    except IntegrityError:
        db.session.rollback()
        return {"error": "Database integrity violation"}, 500

    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 500
