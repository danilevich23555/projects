import os
path = os.path.join(os.getcwd(), 'test.json')


def tokens():
    with open('vk_token.txt', 'r') as token_vk:
        token_vk = token_vk.read().strip()
    with open('ya_token.txt', 'r') as token_ya:
        token_ya = token_ya.read().strip()
    return [token_vk, token_ya]
