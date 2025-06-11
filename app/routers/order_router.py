from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.order_schema import OrderCreate, OrderResponse
from app.models.user import User
from app.services.dependencies import get_current_user
from app.services.order_service import (
    create_order,
    get_orders_by_user,
    get_order_by_id,
    update_order,
    delete_order_by_id,
)

router = APIRouter(prefix="/orders", tags=["Orders"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@router.post("/", response_model=OrderResponse)
def create_user_order(order: OrderCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return create_order(db, user_id=current_user.id, order_data=order)

@router.get("/", response_model=List[OrderResponse])
def list_user_orders(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return get_orders_by_user(db, current_user.id)

@router.put("/{order_id}", response_model=OrderResponse)
def update_user_order(order_id: int, order: OrderCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_order = get_order_by_id(db, order_id)
    if not db_order or db_order.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found or access denied")
    return update_order(db, order_id, order)

@router.delete("/{order_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user_order(order_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_order = get_order_by_id(db, order_id)
    if not db_order or db_order.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found or access denied")
    delete_order_by_id(db, order_id)
