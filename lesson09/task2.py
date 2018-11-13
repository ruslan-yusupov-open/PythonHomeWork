# при помощи библиотеки requests нужно скачать содержимое страниц
# reddit.com/r/python (любой тред > 5 комментариев) и вывести пару: автор
# комментария и его текст в консоль

# -*- coding: utf-8 -*-
import re
import requests

MIN_COMMENTS = 5

REQUEST_HEADERS = {
    'User-agent': 'Mozilla/5.0'
}


def get_reddit():
    r = requests.get('http://reddit.com/r/python', headers=REQUEST_HEADERS)

    import re

    pattern = r'<a [^>]+? href=\"([^\">]+?)\" [^>]+?>.*?(\d+) comments'

    result = re.findall(pattern, str(r.content))
    result = list(filter(lambda item: (int(item[1]) > MIN_COMMENTS), result))

    if len(result) > 0:
        res_item = result[0]
        print("url {}".format(res_item[0]))
        return res_item[0]
    else:
        return None


def print_comments(url):
    # лайфхак - используем старую версию реддита, которая чуть более понятна
    url = url.replace("https://www.reddit.com", "https://old.reddit.com")

    r2 = requests.get(url, headers=REQUEST_HEADERS)

    str_content = str(r2.content)

    search = re.search(r'<div class="content" role="main"[^>]*?>(.+?)<div class="footer-parent"[^>]*?>', str_content)

    if search:
        str_content = search.group(1)

    name_pattern_group = r'<a href="[^"]+/user/([^"]+)"[^>]*?class="author'  # [^"+]"[^>]*?>([^<]*?)</a>'
    names = re.findall(name_pattern_group, str_content)

    name_pattern_group = r'<div class="usertext-body[^>]*?>[^<]*?<div class="md">(.+?)</div>'
    comments = re.findall(name_pattern_group, str_content)

    names_comments = zip(names, comments)
    for name_comment in names_comments:
        print("name: {}, comment: {}".format(name_comment[0], name_comment[1]))


if __name__ == '__main__':
    site_url = get_reddit()

    if site_url:
        print_comments(site_url)
