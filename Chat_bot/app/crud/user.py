from sqlalchemy.orm import Session
from app import models, schemas

def create_habit(db: Session, habit: schemas.HabitCreate, user_id: int):
    db_habit = models.Habit(name=habit.name, description=habit.description, user_id=user_id)
    db.add(db_habit)
    db.commit()
    db.refresh(db_habit)
    return db_habit

def get_habits(db: Session, user_id: int):
    return db.query(models.Habit).filter(models.Habit.user_id == user_id).all()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(email=user.email, full_name=user.full_name, hashed_password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()
