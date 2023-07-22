"""
        Code to convert the tabular data into a document oriented format
    :param tabular data
    :return posts
"""
import pandas as pd


def transforming_data(data):
    """
        Transformation of the data from tabular to document format
    :param data: dict with the tabular data
    :return: dict based in json document format
    """

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
    """
        Document creation function
    :param sub_df: dataframe subset
    :param index: data position in the dataframe
    :return:
    """
    documents = {
        "id_pedido": (sub_df['id_order'][index]).item(),
        "id_customer": (sub_df['id_customer'][index]).item(),
        "local": {
            "city": sub_df['city'][index],
            "state": sub_df['state'][index],
            "country": sub_df['country'][index]
        },
        # "order_date": datetime.datetime(sub_df['order_date'][index]),
        "order_status": sub_df['status'][index],
        "products": [
            {
                "id_product": sub_df['id_product'][index],
                "name": sub_df['name'][index],
                "category": sub_df['id_product'][index],
                "quantity": (sub_df['quantity'][index]).item(),
                "price": float(sub_df['price'][index])
            }
        ],
    }

    return documents

def  appending_doc_data(documents, sub_df, index):
    """
        Suport function for the orginal function: document_creation()
    :param documents: dict with the json document format
    :param sub_df: dataframe subset
    :param index: data position
    :return: data appended to the dict
    """
    # adiciona os demais produtos
    documents['products'].append(
        {
            "id_product": sub_df['id_product'][index],
            "name": sub_df['name'][index],
            "category": sub_df['id_product'][index],
            "quantity": (sub_df['quantity'][index]).item(),
            "price": float(sub_df['price'][index])
        }
    )
