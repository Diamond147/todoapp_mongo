def user_serializer(user_document) -> dict:
    """Converts a MongoDB user object to a Python dictionary"""
    return {
        "id": str(user_document.get("_id")),
        "name": user_document.get("name"),
        "email": user_document.get("email"),
        "created_at": user_document.get("created_at")
    }


def users_serializer(users_documents) -> list:
    """Converts a MongoDB cursor object to a list of Python dictionaries"""
    user_lists = []
    for user_document in users_documents:
        user_lists.append(user_serializer(user_document))
    return user_lists
