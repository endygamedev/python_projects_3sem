"""
    Задачи:
        1. Взять любой простой сайт
        2. Вывести его Headers
        3. Вывести его закодированный через base64 html код
        4. Используя закодированный код и модуль http.server, создайте локальный сервер, где будет выводиться заглавная страница этого сайта
"""


import urllib.request
import base64
from http.server import HTTPServer, BaseHTTPRequestHandler


response = urllib.request.urlopen('https://endygamedev.github.io/')

# Headers
headers = response.info()
# print(headers)

# Закодированный через base64 html код
my_url = 'https://endygamedev.github.io/'
my_headers = {'Content-Type': 'text/html; charset=utf-8'}

req = urllib.request.Request(url=my_url, headers=my_headers)
response = urllib.request.urlopen(req)
html = response.read()
print(html)

encoded = base64.b64encode(html)
print(encoded)


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(300)
        self.end_headers()
        self.wfile.write(encoded)


httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()