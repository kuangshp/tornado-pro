#coding=utf-8
#用户登录试图
from handlers.base.base_handler import BaseHandler
from datetime import datetime
from models.user.user_model import user_model
class LoginHandler(BaseHandler):
    def get(self):
        self.render("user/login.html", next=self.get_argument("next"))

    def post(self):
        username = self.get_argument("username", "")
        password = self.get_argument("password", "")

        #根据用户名去查找数据库
        search_user = user_model.by_name(username)
        if search_user and search_user.auth_password(password):
            #登录成功调用方法
            self.success_login(search_user)
            self.redirect(self.get_argument("name"))
        else:
            self.write(u"登录失败")

    #登录成功附加别的属性
    def success_login(self, user):
        user.last_login = datetime.now()
        user.loginnum += 1
        self.db.add(user)
        self.db.commit()
        self.session.set('username', user.user_name)