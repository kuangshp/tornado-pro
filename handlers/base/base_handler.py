#coding=utf-8
import tornado.escape
from pycket.session import SessionMixin
import tornado.websocket
import tornado.web
from pycket.session import SessionMixin
from libs.db.dbsession import dbSession
from models.user.user_model import user_model


class BaseHandler(tornado.web.RequestHandler, SessionMixin):
    def initialize(self):
        self.db=dbSession

    def get_current_user(self):
        if self.session.get("username"):
            return user_model.by_name(self.session.get("username"))
        else:
            return None

    def on_finish(self):
        self.db.close()


class BaseWebSocket(tornado.websocket.WebSocketHandler, SessionMixin):
    def get_current_user(self):
        if self.session.get("username"):
            return user_model.by_name(self.session.get("username"))
        else:
            return None