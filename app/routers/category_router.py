from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.category_schema import CategoryCreate, CategoryResponse
from app.services.category_service import (
    create_category,
    get_categories,
    update_category,
    delete_category_by_id,
    get_category_by_id,
)
from app.services.dependencies import require_admin
from app.database import SessionLocal

router = APIRouter(prefix="/categories", tags=["Categories"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=CategoryResponse)
def create(category: CategoryCreate, db: Session = Depends(get_db), _=Depends(require_admin)):
    return create_category(db, category)

@router.get("/", response_model=list[CategoryResponse])
def list_categories(db: Session = Depends(get_db)):
    return get_categories(db)

@router.put("/{category_id}", response_model=CategoryResponse)
def update(category_id: int, category: CategoryCreate, db: Session = Depends(get_db), _=Depends(require_admin)):
    db_category = get_category_by_id(db, category_id)
    if not db_category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    return update_category(db, category_id, category)

@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(category_id: int, db: Session = Depends(get_db), _=Depends(require_admin)):
    db_category = get_category_by_id(db, category_id)
    if not db_category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    delete_category_by_id(db, category_id)
