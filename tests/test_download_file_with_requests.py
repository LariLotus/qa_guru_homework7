import os.path

import requests

PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
RESOURCES_PATH = os.path.join(PROJECT_ROOT_PATH, '../resources')

def test_downloaded_file_size():
    # TODO сохранять и читать из tmp, использовать универсальный путь

    url = 'https://selenium.dev/images/selenium_logo_square_green.png'

    r = requests.get(url)
    tmp = os.path.join(RESOURCES_PATH, 'selenium_logo.png', )
    with open(tmp, 'wb') as file:
        file.write(r.content)

    size = os.path.getsize(tmp)

    assert size == 30803

