"""
        Code to convert the tabular data into a document oriented format
    :param tabular data
    :return posts
"""
import pandas as pd
import datetime


def transformig_data(data):

    #creating a dict
    dict_df = {}
    for element in data:
        dict_df.update(element)

    df = pd.DataFrame.from_dict(data)
    ids = []

    for element in df['id_order'].tolist():
        if element not in ids:
            ids.append(element)

    documents_list = []

    for code in ids:
        sub_df = (df.loc[lambda df: df['id_order'] == code])
        i = sub_df.index.tolist()[0]
        index_range = [i, i+len(sub_df)]
        documents = None

        for index in range(index_range[0], index_range[1]):
            if documents is None:
                documents = document_creation(sub_df, index)
            else:
                appending_doc_data(documents, sub_df, index)

        documents_list.append(documents)

    return documents_list


def document_creation(sub_df, index):

    documents = {
        "id_pedido": int(sub_df['id_order'][index]),
        "id_customer": int(sub_df['id_customer'][index]),
        "local": {
            "city": sub_df['city'][index],
            "state": sub_df['state'][index],
            "country": sub_df['country'][index]
        },
        # "order_date": datetime.datetime(sub_df['order_date'][index]),
        "order_status": sub_df['status'][index],
        "products": [
            {
                "id_product": str(sub_df['id_product'][index]),
                "name": sub_df['name'][index],
                "category": sub_df['id_product'][index],
                "quantity": int(sub_df['quantity'][index]),
                "price": float(sub_df['price'][index])
            }
        ],
    }

    return documents

def  appending_doc_data(documents, sub_df, index):
    # adiciona os demais produtos
    documents['products'].append(
        {
            "id_product": sub_df['id_product'][index],
            "name": sub_df['name'][index],
            "category": sub_df['id_product'][index],
            "quantity": sub_df['quantity'][index],
            "price": sub_df['price'][index]
        }
    )