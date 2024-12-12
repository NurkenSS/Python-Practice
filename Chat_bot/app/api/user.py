from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import SessionLocal
from app.auth import get_current_user

router = APIRouter()

@router.post("/register", response_model=schemas.User)
def register_user(user: schemas.UserCreate, db: Session = Depends(SessionLocal)):
    """
    Регистрация нового пользователя.
    """
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email is already registered")
    return crud.create_user(db=db, user=user)

@router.get("/profile", response_model=schemas.User)
def get_user_profile(db: Session = Depends(SessionLocal), user_id: int = Depends(get_current_user)):
    """
    Получить профиль текущего пользователя.
    """
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
