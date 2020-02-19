import json
import requests
from woocommerce import API
import random
import datetime

def get_wcapi_obj (params: {}) -> object:
    wcapi = API(
        url=params["url"],
        consumer_key=params["consumer_key"],
        consumer_secret=params["consumer_secret"],
        wp_api=True,
        version="wc/v3",
        query_string_auth=True
    )
    return wcapi

def get_product_by_id (params: {}) -> {}:
    wcapi = get_wcapi_obj(params)
    product_url = "products/" + params["id"]
    return (wcapi.get(product_url).json())

def get_draft_products_id_list(wcapi_obj: object) -> []:
    product_id_list = []
    res = wcapi_obj.get("products?page=1&per_page=100&status=draft").json()
    for product in res:
        product_id_list.append(product["id"])
    res = wcapi_obj.get("products?page=2&per_page=100&status=draft").json()
    for product in res:
        product_id_list.append(product["id"])
    return(product_id_list)

def publish_random_product (params: {}) -> {}:
    wcapi = get_wcapi_obj(params)
    product_ids = get_draft_products_id_list(wcapi)
    selected_product_id = random.choice(product_ids)
    
    data = {
        "status": "publish",
        "date_created": datetime.datetime.now().isoformat(timespec='seconds'),
        "date_created_gmt": datetime.datetime.now().isoformat(timespec='seconds'),
        "date_modified": datetime.datetime.now().isoformat(timespec='seconds'),
        "date_modified_gmt": datetime.datetime.now().isoformat(timespec='seconds')
    }
    product_url = "products/" + str(selected_product_id)
    return (wcapi.put(product_url, data).json())