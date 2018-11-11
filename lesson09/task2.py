# при помощи библиотеки requests нужно скачать содержимое страниц
# reddit.com/r/python (любой тред > 5 комментариев) и вывести пару: автор
# комментария и его текст в консоль

# -*- coding: utf-8 -*-

import requests

MIN_COMMENTS = 5

REQUEST_HEADERS = {
    'User-agent': 'Mozilla/5.0'
}


def get_reddit():
    r = requests.get('http://reddit.com/r/python', headers=REQUEST_HEADERS)

    import re

    pattern = r'<a [^>]+? href=\"([^\">]+?)\" [^>]+?>.*?(\d+) comments'

    # print(str(r.content))

    result = re.findall(pattern, str(r.content))

    url = None

    for res_item in result:
        if int(res_item[1]) >= MIN_COMMENTS:
            url = res_item[0]
            print(res_item)
            break

    return url


def get_comments(url):
    r = requests.get('http://reddit.com/r/python', headers=REQUEST_HEADERS)

    r2 = requests.get(url, headers=REQUEST_HEADERS)

    print(str(r2.content))


if __name__ == '__main__':
    #    url = get_reddit()
    page_url = "https://www.reddit.com/r/Python/comments/9vsvou/python_job_opportunities_and_a_little_roadmap/"


