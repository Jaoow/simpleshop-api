from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    category_id: int

class ProductResponse(BaseModel):
    id: int
    name: str
    description: str
    price: float
    category_id: int

    class Config:
        from_attributes = True
