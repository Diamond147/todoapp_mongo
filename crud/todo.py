from serializers.todo import todo_serializer, todos_serializer
from fastapi.encoders import jsonable_encoder
from bson.objectid import ObjectId
from schemas.todo import TodoCreate, TodoUpdate
from database import todo_collection


class TodoCrud:

    @staticmethod
    def create_todo(todo_data: TodoCreate):
        todo_data = jsonable_encoder(todo_data)
        todo_document_data = todo_collection.insert_one(todo_data)
        todo_id = todo_document_data.inserted_id
        todo = todo_collection.find_one({"_id": ObjectId(todo_id)})
        return todo_serializer(todo)
    

    @staticmethod
    def list_todos():
        todos = todo_collection.find()

        return todos_serializer(todos)


    @staticmethod
    def get_todo(todo_id: str):
        todo = todo_collection.find_one({"_id": ObjectId(todo_id)})
        return todo_serializer(todo)
    

    @staticmethod
    def update_todo(todo_id: str, todo_data: TodoUpdate):
        todo = todo_collection.find_one({"_id": ObjectId(todo_id)})

        if not todo:
            return None
        
        todo_dict = todo_data.model_dump(exclude_unset=True)  # Exclude unset fields

        todo_update = todo_collection.find_one_and_update({"_id": ObjectId(todo_id)}, {"$set": todo_dict}, return_document=True)

        return todo_serializer(todo_update)
    

    @staticmethod
    def delete_todo(todo_id: str):
        todo = todo_collection.delete_one({"_id": ObjectId(todo_id)})
        return todo
    

    @staticmethod
    def list_todo_by_user(user_id: str):
        todos = todo_collection.find({"user_id": user_id})

        return todos_serializer(todos)


todo_crud = TodoCrud()
