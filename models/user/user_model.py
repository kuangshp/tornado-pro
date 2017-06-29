#coding=utf-8
#coding=utf-8
from uuid import uuid4
from datetime import datetime
from string import printable

from pbkdf2 import PBKDF2
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (create_engine, Column, Integer, String,
                        Text, Boolean, Date, DateTime, ForeignKey)

from libs.db.dbsession import Base
from libs.db.dbsession import dbSession


class user_model(Base):
    __tablename__ = 'user1'
    uuid = Column(String(36), unique=True, nullable=False, default=lambda: str(uuid4()))
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String(50), nullable=False)
    _password = Column('password', String(64))
    createtime = Column(DateTime, default=datetime.now)
    update_time = Column(DateTime)
    last_login = Column(DateTime)
    loginnum = Column(Integer, default=0)
    _locked = Column(Boolean, default=False, nullable=False)

    _avatar = Column(String(64))


    def _hash_password(self, password):
        return PBKDF2.crypt(password, iterations=0x2537)


    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = self._hash_password(password)

    def auth_password(self, other_password):
        if self._password:
            return self.password == PBKDF2.crypt(other_password, self.password)
        else:
            return False

    @property
    def avatar(self):
        return self._avatar if self._avatar else "default_avatar.jpeg"


    @avatar.setter
    def avatar(self, image_data):
        class ValidationError(Exception):
            def __init__(self, message):
                super(ValidationError, self).__init__(message)
        if 64 < len(image_data) < 1024 * 1024:
            import imghdr
            import os
            ext = imghdr.what("", h=image_data)
            print ext
            print self.uuid
            if ext in ['png', 'jpeg', 'gif', 'bmp'] and not self.is_xss_image(image_data):
                if self._avatar and os.path.exists("static/images/useravatars/" + self._avatar):
                    os.unlink("static/images/useravatars/" + self._avatar)
                file_path = str("static/images/useravatars/" + self.uuid + '.' + ext)

                with open(file_path, 'wb') as f:
                    f.write(image_data)

                self._avatar = self.uuid + '.' + ext
            else:
                raise ValidationError("not in ['png', 'jpeg', 'gif', 'bmp']")
        else:
            raise ValidationError("64 < len(image_data) < 1024 * 1024 bytes")

    def is_xss_image(self, data):
        return all([char in printable for char in data[:16]])

    @classmethod
    def all(cls):
        return dbSession.query(cls).all()

    @classmethod
    def by_id(cls, id):
        return dbSession.query(cls).filter_by(id=id).first()

    @classmethod
    def by_uuid(cls, uuid):
        return dbSession.query(cls).filter_by(uuid=uuid).first()

    @classmethod
    def by_name(cls, name):
        return dbSession.query(cls).filter_by(user_name=name).first()

    @property
    def locked(self):
        return self._locked



    @locked.setter
    def locked(self, value):
        assert isinstance(value, bool)
        self._locked = value


    def to_dict(self):
        return {
            'id': self.id,
            'user_name': self.user_name,
            'last_login': self.last_login,
        }

    def __repr__(self):
        return u'<User1 - id: %s  name: %s>' % (self.id,self.user_name)
