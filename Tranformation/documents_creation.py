"""
        Code to convert the tabular data into a document oriented format
    :param tabular data
    :return posts
"""
import pandas as pd
import json

def transformig_data(data):

    #creating a dict
    dict_df = {}
    for element in data:
        dict_df.update(element)

    df = pd.DataFrame.from_dict(data)
    ids = df['id_order'].tolist()

    for code in ids:
        sub_df = (df.loc[lambda df: df['id_order'] == code])
        documents = None
        for index in range(0, len(sub_df)):
            print(sub_df['id_order'][index])

            if documents is None:
                documents = {
                        "id_pedido": sub_df['id_order'][index],
                        "id_customer": sub_df['id_customer'][index],
                        # "id_vendedor": 1350,
                        "local": {
                            "city": sub_df['city'][index],
                            "state": sub_df['state'][index],
                            "country":  sub_df['country'][index]
                        },
                        "order_date": sub_df['order_date'][index],
                        "order_status":  sub_df['status'][index],
                        "products": [
                            {
                                "id_product": 123,
                                "name": "",
                                "category": "",
                                "price": 12.1
                            },
                        ],
                }
            else:
                # adiciona os demais produtos
                pass

            print(documents['products'])
            input()

    return data

def inserting_data_posts(db, posts, collection_name: str):
    collection = db.get_collection(collection_name)
    if type(posts) is str:
        post_id = collection.insert_one(posts).inserted_id
    else:
        post_id = collection.insert_many(posts).inserted_id
    return post_id
