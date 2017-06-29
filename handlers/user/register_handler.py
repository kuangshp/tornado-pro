#coding=utf-8
#用户注册的视图
from handlers.base.base_handler import BaseHandler
from models.user.user_model import user_model
class RegisterHandler(BaseHandler):
    def get(self):
        self.render("user/register.html")

    def post(self):
        username = self.get_argument("name", "")
        password = self.get_argument("pass", "")
        if not username and not password:
            self.write(u"用户名或密码输入有错误")
        # 先查询数据库是否已经存在该用户
        search_name = user_model.by_name(username)
        if search_name:
            self.write(u"该用户名已经存在，不能重复注册")
        else:
            user = user_model()
            user.user_name = username
            user.password = password
            self.db.add(user)
            self.db.commit()
            self.write(u"注册成功")