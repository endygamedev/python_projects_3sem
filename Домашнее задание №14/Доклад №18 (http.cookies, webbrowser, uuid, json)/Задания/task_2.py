"""
    Создайте функцию в которой пользователь вводит ссылку сайта и получает данные cookie по странице.
"""

from urllib.request import Request, build_opener, HTTPCookieProcessor, HTTPHandler, HTTPSHandler
import http.cookiejar


def fetch(opener, url):
    req = Request(url)
    return opener.open(req)


def dump(cookies):
    for cookie in cookies:
        print(cookie.name, cookie.value)


def get_cookie(url):
    url = url
    cookies = http.cookiejar.LWPCookieJar()
    handlers = [
        HTTPHandler(),
        HTTPSHandler(),
        HTTPCookieProcessor(cookies)
    ]

    opener = build_opener(*handlers)

    fetch(opener, url)
    dump(cookies)


get_cookie('http://www.google.com/')