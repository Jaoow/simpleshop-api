from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.order_schema import OrderCreate, OrderResponse
from app.models.user import User
from app.services.dependencies import get_current_user
from app.services.order_service import create_order, get_orders_by_user

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