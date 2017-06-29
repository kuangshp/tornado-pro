#coding=utf-8
from login_handler import LoginHandler
from register_handler import RegisterHandler
user_urls = [
    (r"/login",LoginHandler),
    (r"/register",RegisterHandler)
]