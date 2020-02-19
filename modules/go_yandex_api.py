import requests
import json

def translate_text (text: str, target_lang: str, key: str) -> {}:
    
    api_endpoint = "https://translate.yandex.net/api/v1.5/tr.json/translate"
    payload = {
        "key": key,
        "text": text.strip().replace('\n','').replace('\t',''),
        "lang": target_lang,
        "format": "html"
    }
    
    res = requests.post(api_endpoint, data=payload)
    return res.json()

def rewrite_text (text: str, key: str) -> {}:
    res_es = translate_text(
        text=text,
        target_lang='es',
        key=key
    )
    res_pl = translate_text(
        text=res_es["text"][0],
        target_lang='pl',
        key=key
    )
    res_en = translate_text(
        text=res_pl["text"][0],
        target_lang='en',
        key=key
    )
    return (res_en)