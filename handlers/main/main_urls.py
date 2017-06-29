#coding=utf-8
from main_handler import MainHandler
from handlers.user.user_urls import user_urls
handlers = [
    (r'/', MainHandler),
]

handlers += user_urls
