from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.category_schema import CategoryCreate, CategoryResponse
from app.services.category_service import create_category, get_categories
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
