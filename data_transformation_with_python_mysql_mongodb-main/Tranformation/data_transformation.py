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

    ids = set(element for element in df['id_order'].tolist())

    documents_list = []

    for code in ids:
        sub_df = df.loc[lambda df: df['id_order'] == code]
        i = sub_df.index.to_list()[0]
        index_range = [i, i+len(sub_df)]
        document = None

        for index in range(index_range[0], index_range[1]):
            if document is None:
                document = document_creation(sub_df, index)
            else:
                appending_doc_data(document, sub_df, index)

        documents_list.append(document)
    return documents_list


def document_creation(sub_df, index):
    """
        Document creation function
        :param sub_df: dataframe subset
        :param index: data position in the dataframe
        :return documents: data formatted in JSON
    """
    documents = {
        "id_order": (sub_df['id_order'][index]).item(),
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


def appending_doc_data(document, sub_df, index):
    """
        Suport function for the orginal function: document_creation()
        :param documents: dict with the json document format
        :param sub_df: dataframe subset
        :param index: data position
        :return: data appended to the dict
    """
    document['products'].append(
        {
            "id_product": sub_df['id_product'][index],
            "name": sub_df['name'][index],
            "category": sub_df['id_product'][index],
            "quantity": (sub_df['quantity'][index]).item(),
            "price": float(sub_df['price'][index])
        }
    )
