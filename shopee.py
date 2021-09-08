from fastapi import FastAPI
import requests
import json

app = FastAPI()

@app.get('/getitem')
def getitem(item_id: str, shop_id: str):
    return json.loads(requests.get(f'https://shopee.com.my/api/v4/item/get?itemid={item_id}&shopid={shop_id}').text)

@app.get('/searchitem')
def searchitem(keyword: str="rickroll", max_limit: int=5):
    return json.loads(requests.get(f'https://shopee.com.my/api/v4/search/search_items?by=relevancy&keyword={keyword}&limit={max_limit}&newest=0&order=desc&page_type=search&scenario=PAGE_GLOBAL_SEARCH&version=2').text)
