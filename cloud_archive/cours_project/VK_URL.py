import requests
from settings import tokens

def get_VK_URL():
    URL = 'https://api.vk.com/method/photos.get'
    owner_id = input('Введите ID пользователя VK: ')
    params = {
        'owner_id': owner_id,
        'album_id': 'profile',
        'extended': 1,
        'access_token': tokens()[0],
        'v': '5.131'
    }
    resp = requests.get(URL, params=params)
    quntity_foto = (len((resp.json()['response']['items'])))
    temp = []
    log = []
    for foto in range(quntity_foto):
        url = (resp.json()['response']['items'][foto])['sizes'][-1]['url']
        like = (resp.json()['response']['items'][foto]['likes']['count'])
        size = (resp.json()['response']['items'][0])['sizes'][-1]['type']
        temp.append({'url': url, 'like': like})
        log.append({'file name': like, 'size': size})
    return [temp, log]
