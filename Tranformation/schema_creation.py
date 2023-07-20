
def collection_creation():
    pass

def document_creation(sub_df, index):

    documents = {
        "id_pedido": sub_df['id_order'][index],
        "id_customer": sub_df['id_customer'][index],
        # "id_vendedor": 1350,
        "local": {
            "city": sub_df['city'][index],
            "state": sub_df['state'][index],
            "country": sub_df['country'][index]
        },
        "order_date": sub_df['order_date'][index],
        "order_status": sub_df['status'][index],
        "products": [
            {
                "id_product": sub_df['id_product'][index],
                "name": sub_df['name'][index],
                "category": sub_df['id_product'][index],
                "quantity": sub_df['quantity'][index],
                "price": sub_df['price'][index]
            }
        ],
    }

    return documents

def  appending_json_data(documents, sub_df, index):
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