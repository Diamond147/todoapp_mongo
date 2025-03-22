from fastapi import APIRouter, HTTPException
from crud.user import user_crud
from schemas.user import User, UserCreate, UserUpdate
from pymongo.errors import DuplicateKeyError

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=User)
def create_user_endpoint(user: UserCreate):
    try:
        new_user = user_crud.create_user(user)
        # return {"data": new_user, "message": "User created successfully"}
        return new_user
    
    except DuplicateKeyError:
        raise HTTPException(status_code=400, detail="User with this email already exists")


@router.get("/", response_model=list[User])
def list_users_endpoint():
    return user_crud.list_users()


@router.get("/{user_id}", response_model=User)
def get_user_endpoint(user_id: str):
    user = user_crud.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.put("/{user_id}", response_model=User)
def Update_user_endpoint(user_id: str, user_data: UserUpdate):
    update_data = user_crud.update_user(user_id, user_data)
    if not update_data:
        raise HTTPException(status_code=404, detail="User not found")
    return update_data


@router.delete("/{user_id}")
def delete_user_endpoint(user_id: str):
    user = user_crud.delete_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}


