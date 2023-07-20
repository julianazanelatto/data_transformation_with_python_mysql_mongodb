import pymongo

def inserting_data_posts(db, posts, collection_name: str):
    collection = db.get_collection(collection_name)
    if type(posts) is str:
        post_id = collection.insert_one(posts).inserted_id
    else:
        post_id = collection.insert_many(posts).inserted_id
    return post_id