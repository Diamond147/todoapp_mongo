from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr



class UserBase(BaseModel):
    name: str = "Opeyemi"
    email: EmailStr = "Opeyemi@gmail.com"
    created_at: datetime = datetime.now()


class User(UserBase):
    id: str


class UserCreate(UserBase):
    pass


class UserUpdate(BaseModel):
    name: Optional[str] = "Opeyemi1"
    email: Optional[EmailStr] = "Opeyemi1@gmail.com"
    created_at: Optional[datetime] = datetime.now()
