# python3 -m venv virtualenv
# source virtualenv/bin/activate
# pip install requests woocommerce datetime
# ibmcloud login -r eu-gb
# ibmcloud target --cf
# zip -r surrenders_publish_random_product.zip virtualenv __main__.py go_wcapi.py
# ibmcloud fn action create surrenders_publish_random_product surrenders_publish_random_product.zip --kind python:3.7 --main main
# ibmcloud fn action update surrenders_luca-ia-webhooks-api surrenders_publish_random_product.zip --kind python:3.7 --main main

from go_wcapi import publish_random_product

def main(params):
    res = publish_random_product(params)
    return (res)
