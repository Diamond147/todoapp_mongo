from typing import Optional
from pydantic import BaseModel


class TodoBase(BaseModel):
    user_id: str
    title: str = "A new todo"
    description: str = "A new todo description"
    is_completed: bool = False


class Todo(TodoBase):
    id: str

class TodoCreate(TodoBase):
    pass


class TodoUpdate(BaseModel):
    user_id: Optional[str]
    title: Optional[str] = "An updated todo"
    description: Optional[str] = "A new updated todo"
    is_completed: Optional[bool] = True
