import pymongo
from serializers.user import user_serializer, users_serializer 
from fastapi.encoders import jsonable_encoder
from bson.objectid import ObjectId
from schemas.user import UserCreate, UserUpdate
from database import user_collection


class UserCrud:

    @staticmethod
    def create_user(user_data: UserCreate):
        
        user_collection.create_index([("email", pymongo.ASCENDING)], unique=True, sparse=True)

        user_data = jsonable_encoder(user_data)
        user_document_data = user_collection.insert_one(user_data)
        user_id = user_document_data.inserted_id
        user = user_collection.find_one({"_id": ObjectId(user_id)})
        return user_serializer(user)
    
    
    @staticmethod
    def list_users():
        users = user_collection.find()  # This returns a cursor
        
        return users_serializer(users)


    @staticmethod
    def get_user(user_id: str):
        user = user_collection.find_one({"_id": ObjectId(user_id)})
        return user_serializer(user)
    

    @staticmethod
    def update_user(user_id: str, user_data: UserUpdate):
        user = user_collection.find_one({"_id": ObjectId(user_id)})

        if not user:
            return None
        
        user_dict = user_data.model_dump(exclude_unset=True)  # Exclude unset fields

        user_updated = user_collection.find_one_and_update({"_id": ObjectId(user_id)}, {"$set": user_dict}, return_document=True)

        return user_serializer(user_updated)


    @staticmethod
    def delete_user(user_id: str):
        user = user_collection.delete_one({"_id": ObjectId(user_id)})
        return user
            

user_crud = UserCrud()



