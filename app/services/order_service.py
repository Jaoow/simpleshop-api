from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.order import Order, OrderItem
from app.models.product import Product
from app.schemas.order_schema import OrderCreate

def create_order(db: Session, user_id: int, order_data: OrderCreate):
    # Criar o pedido
    order = Order(user_id=user_id)
    db.add(order)
    db.flush()  # gera o ID do pedido para associar os itens

    for item in order_data.items:
        product = db.query(Product).filter(Product.id == item.product_id).first()
        if not product:
            raise HTTPException(status_code=404, detail=f"Produto com ID {item.product_id} não encontrado")

        order_item = OrderItem(
            order_id=order.id,
            product_id=item.product_id,
            quantity=item.quantity
        )
        db.add(order_item)

    db.commit()
    db.refresh(order)
    return order

def get_orders_by_user(db: Session, user_id: int):
    return db.query(Order).filter(Order.user_id == user_id).all()

def get_order_by_id(db: Session, order_id: int, user_id: int):
    order = db.query(Order).filter(Order.id == order_id, Order.user_id == user_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    return order
