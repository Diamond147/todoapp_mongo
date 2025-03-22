from fastapi import APIRouter, HTTPException
from crud.todo import todo_crud
from schemas.todo import Todo, TodoCreate, TodoUpdate

router = APIRouter(prefix="/todos", tags=["Todos"])


@router.post("/", response_model=Todo)
def create_todo_endpoint(todo: TodoCreate):
        new_todo =  todo_crud.create_todo(todo)
        return new_todo


@router.get("/", response_model=list[Todo])
def list_todos_endpoint():
    return todo_crud.list_todos()


@router.get("/{todo_id}", response_model=Todo)
def get_todo_endpoint(todo_id: str):
    todo = todo_crud.get_todo(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@router.put("/{todo_id}", response_model=Todo)
def Update_todo_endpoint(todo_id: str, todo_data: TodoUpdate):
    update_data = todo_crud.update_todo(todo_id, todo_data)
    if not update_data:
        raise HTTPException(status_code=404, detail="Todo not found")
    return update_data


@router.delete("/{todo_id}")
def delete_todo_endpoint(todo_id: str):
    todo = todo_crud.delete_todo(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"message": "Todo deleted successfully"}



@router.get("/user/{user_id}")
def list_todo_by_user_endpoint(user_id: str):
        todos = todo_crud.list_todo_by_user(user_id)
        
        if not todos:
            raise HTTPException(status_code=401, detail= "todos not found")
            
        return todos