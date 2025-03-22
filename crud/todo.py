from serializers.todo import todo_serializer
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

        todo_list = []
        for todo in todos:
            todo_list.append(todo_serializer(todo))

        return todo_list

        # OR
        # return [todo_serializer(todo) for todo in todos]


    @staticmethod
    def get_todo(todo_id: str):
        todo = todo_collection.find_one({"_id": ObjectId(todo_id)})
        return todo_serializer(todo)
    

    @staticmethod
    def update_todo(todo_id: str, todo_data: TodoUpdate):
        update_data = {}
        for k,v in todo_data.model_dump().items():
            if v is not None:
                update_data[k] = v
                
        if update_data:    
            todo_collection.update_one({"_id": ObjectId(todo_id)}, {"$set": update_data})
        return todo_serializer(todo_collection.find_one({"_id": ObjectId(todo_id)}))
    

    @staticmethod
    def delete_todo(todo_id: str):
        todo = todo_collection.delete_one({"_id": ObjectId(todo_id)})
        return todo
    

    @staticmethod
    def list_todo_by_user(user_id: str):
        todos = todo_collection.find({"user_id": user_id})
        
        todo_list = []
        for todo in todos:
            todo_list.append(todo_serializer(todo))
            
        return todo_list


todo_crud = TodoCrud()
