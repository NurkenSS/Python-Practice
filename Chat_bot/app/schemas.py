from pydantic import BaseModel
from typing import List

class HabitBase(BaseModel):
    name: str
    description: str

class HabitCreate(HabitBase):
    pass  

class Habit(HabitBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True 
        
class UserBase(BaseModel):
    email: str
    full_name: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True
