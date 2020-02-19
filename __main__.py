# python3 -m venv virtualenv
# virtualenv virtualenv
# source virtualenv/bin/activate
# pip install requests woocommerce datetime
# ibmcloud login -r eu-gb
# ibmcloud target --cf
# zip -r a4f.zip virtualenv modules __main__.py go_wcapi.py

from go_wcapi import publish_random_product
from modules.go_yandex_api import rewrite_text

# ibmcloud fn action create surrenders_publish_random_product a4f.zip --kind python:3.7 --main main
# ibmcloud fn action update surrenders_luca-ia-webhooks-api a4f.zip --kind python:3.7 --main main
def main(params):
    res = publish_random_product(params)
    return (res)

# ibmcloud fn action create rewrite_text_function a4f.zip --kind python:3.7 --main rewrite_text_function
# ibmcloud fn action update rewrite_text_function a4f.zip --kind python:3.7 --main rewrite_text_function
def rewrite_text_function(params):
    res = rewrite_text(params["text"], params["key"])
    return (res)