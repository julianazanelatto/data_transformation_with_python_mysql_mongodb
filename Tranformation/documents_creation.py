"""
        Code to convert the tabular data into a document oriented format
    :param tabular data
    :return posts
"""
import pandas as pd

def transformig_data(data):

    #creating a dict
    dict_df = {}
    for element in data:
        dict_df.update(element)

    df = pd.DataFrame.from_dict(data)
    ids = df['id_order'].tolist()

    for code in ids:
        (df.loc[lambda df: df['id_order'] == code])


        documents = {
            "author": "Mike",
            "text": "My first mongodb application based on python",
            "tags": ["mongodb", "python3", "pymongo"],
            "date": ""
        }

    return data

def inserting_data_posts(db, posts, collection_name: str):
    collection = db.get_collection(collection_name)
    if type(posts) is str:
        post_id = collection.insert_one(posts).inserted_id
    else:
        post_id = collection.insert_many(posts).inserted_id
    return post_id
