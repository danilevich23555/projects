import requests
from threading import Thread
import os
import datetime
import time
from threading import Thread




def function_for_thread(id_product):
    HEADERS = {
        'Api-Key': ApiKey,
        'Client-Id': ClientId,
        'Content-type': 'application/json'
    }
    json = {"product_id": id_product}
    url = 'https://api-seller.ozon.ru/v1/product/info/description'
    response3 = requests.post(url=url, headers=HEADERS, json=json)
    return print(response3.json()["result"]["name"])

def run_threads(data:list):
        threads = [
            Thread(target=function_for_thread, args=(data[i],))
            for i in range(0, len(data))
        ]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()


ApiKey='236f59a6-0906-4ae8-8109-ae089a42c0b0'
ClientId='2663'


data = [7223470,7223472,7223515,7223516,7223517,7223548,7223549,7223550,7223570,7223571,7223572,7223573,7223593,7223594,7223595,7335989,7346814,7346815,7346816,7346818,7346819,1192752,7118833,7118835,7118931,7223469,7223470,7223515,7223516,7223517,7223548,7223549,7223550,7223570,7223571,7223572,7223593,7223594,7223595,7335989,7346814,7346815,7346816,1188364,1192752,7118833,7118835,7118931,7118934,7223469,7223470,7223472,7223515,7223516,7223517,7223548,7223549,7223550,7223570,7223571,7223572,7223573,7223593,7223594,7223595,7335989,7346814,7346815,7346816,7346818,7346819,1188364,1192752,7118833,7118835,7118931,7223469,7223470,7223515,7223516,7223517,7223548,7223549,7223550,7223570,7223571,7223572,7223593,7223594,7223595,7335989,7346814,7346815,7346816,1188364,1192752,7118833,7118835,7118931,7118934,7223469,7223470,7223472,7223515,7223516,7223517,7223548,7223549,7223550,7223570,7223571,7223572,7223573,7223593,7223594,7223595,7335989,7346814,7346815,7346816,7346818,7346819]
start1=time.time()
run_threads(data)
print(f'Треды отработали за {time.time()-start1}')


print('------------------------------------------------------------------------------------------------------')




HEADERS =  {
        'Api-Key': ApiKey,
        'Client-Id': ClientId,
        'Content-type': 'application/json'
    }


url = 'https://api-seller.ozon.ru/v1/actions'
response = requests.get(url=url, headers=HEADERS)
temp=[]
print(response.json()['result'])
[temp.append({'id': x['id'], 'title': x['title'], 'date_start': x['date_start'],
              'date_end': x['date_end']}) for x in response.json()['result']]


HEADERS =  {
        'Api-Key': ApiKey,
        'Client-Id': ClientId,
        'Content-type': 'application/json'
    }
for x in response.json()['result']:
    json  = {"action_id": x['id'], "limit": 0, "offset": 0}
    url = 'https://api-seller.ozon.ru/v1/actions/candidates'
    response2 = requests.post(url=url, headers=HEADERS, json=json)
    temp=[]
    start2=time.time()
    for y in response2.json()['result']['products']:
        HEADERS =  {
                'Api-Key': ApiKey,
                'Client-Id': ClientId,
                'Content-type': 'application/json'
            }

        json  = {"product_id": y['id']}
        url = 'https://api-seller.ozon.ru/v1/product/info/description'
        response3 = requests.post(url=url, headers=HEADERS, json=json)
        print(response3.json()["result"]["name"])
print(f'Не треды отработали за {time.time()-start2}')


