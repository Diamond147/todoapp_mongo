from serializers.user import user_serializer 
from fastapi.encoders import jsonable_encoder
from bson.objectid import ObjectId
from schemas.user import UserCreate, UserUpdate
from database import user_collection


class UserCrud:

    @staticmethod
    def create_user(user_data: UserCreate):
        
        user_collection.create_index("email", unique=True)

        user_data = jsonable_encoder(user_data)
        user_document_data = user_collection.insert_one(user_data)
        user_id = user_document_data.inserted_id
        user = user_collection.find_one({"_id": ObjectId(user_id)})
        return user_serializer(user)
    
    
    @staticmethod
    def list_users():
        users = user_collection.find()

        user_list = []
        for user in users:
            user_list.append(user_serializer(user))
            
        return user_list
    
         # OR
        # return [user_serializer(user) for user in users]


    @staticmethod
    def get_user(user_id: str):
        user = user_collection.find_one({"_id": ObjectId(user_id)})
        return user_serializer(user)
    

    @staticmethod
    def update_user(user_id: str, user_data: UserUpdate):
        # user_data = {k: v for k, v in user_data.dict().items() if v is not None} 
        #OR

        update_data = {}
        for k, v in user_data.model_dump().items():
            if v is not None:
                update_data[k] = v

        if update_data:
            user_collection.update_one({"_id": ObjectId(user_id)}, {"$set": update_data})

        return user_serializer(user_collection.find_one({"_id": ObjectId(user_id)}))


    @staticmethod
    def delete_user(user_id: str):
        user = user_collection.delete_one({"_id": ObjectId(user_id)})
        return user
            

user_crud = UserCrud()



