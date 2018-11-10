# при помощи библиотеки requests нужно скачать содержимое страниц
# reddit.com/r/python (любой тред &gt; 5 комментариев) и вывести пару: автор
# комментария и его текст в консоль

# -*- coding: utf-8 -*-

import requests

REQUEST_HEADERS = {
    'User-agent': 'Mozilla/5.0'
}

def get_reddit():
    r = requests.get('http://reddit.com/r/python', headers=REQUEST_HEADERS)
    # print(r.status_code)
    # print(r.headers)
    # print()

    import re

    pattern = r'<a [^>]+? href=\"([^\">]+?)\" [^>]+?>.*?(\d+) comments'

    print(str(r.content))

    result = re.findall(pattern, str(r.content))

    print(result)


if __name__ == '__main__':
    get_reddit()

# find_pet_by_status('sold')


# def find_pet_by_status(status):
#     params = {'status': status}
#     headers = {
#         #'Accept': 'application/xml'
#         'Accept': 'application/json'
#     }
#     url = 'http://petstore.swagger.io/v2/pet/findByStatus'
#     r = requests.get(url, params=params, headers=headers)
#     print(r.status_code, r.headers)
#     print(r.content)
#
#     # s = 'http://petstore.swagger.io/v2/pet/findByStatus?status=sold'
