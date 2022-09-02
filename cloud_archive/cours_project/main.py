from ya_disk import YandexDisk
from settings import tokens
from VK_URL import get_VK_URL
import os
path = os.path.join(os.getcwd(), 'test.json')
import json



if __name__ == '__main__':
    ya = YandexDisk(token=tokens()[1])
    ya.upload_file_to_disk(get_VK_URL()[0])
    with open(path, 'w') as data:
        json.dump(get_VK_URL()[1], data)


