"""
        Code to convert the tabular data into a document oriented format
    :param tabular data
    :return posts
"""
import pandas as pd
import json
from Tranformation.schema_creation import document_creation, appending_json_data


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
                appending_json_data(documents, sub_df, index)

        documents_list.append(documents)

    return documents_list

def cleaning_data():
    pass
