#coding=utf-8
import tornado.web
from handlers.base.base_handler import BaseHandler
class MainHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render("main/index.html")