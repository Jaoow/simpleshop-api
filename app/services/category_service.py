from sqlalchemy.orm import Session
from app.models.category import Category
from app.schemas.category_schema import CategoryCreate

def create_category(db: Session, category: CategoryCreate):
    db_category = Category(name=category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def get_categories(db: Session):
    return db.query(Category).all()

def get_category_by_id(db: Session, category_id: int):
    return db.query(Category).filter(Category.id == category_id).first()

def update_category(db: Session, category_id: int, category_data: CategoryCreate):
    category = get_category_by_id(db, category_id)
    category.name = category_data.name
    db.commit()
    db.refresh(category)
    return category

def delete_category_by_id(db: Session, category_id: int):
    category = get_category_by_id(db, category_id)
    db.delete(category)
    db.commit()
