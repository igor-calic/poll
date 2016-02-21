import logging

from google.appengine.ext import ndb
from google.net.proto.ProtocolBuffer import ProtocolBufferDecodeError

from ferris import BasicModel


class User(BasicModel):
    name = ndb.StringProperty(indexed=True, required=True)

    @classmethod
    def create(cls, name):
        user = User(name=name)
        return user.put()

    @classmethod
    def by_urlsafe_key(cls, user_key):
        user = None
        try:
            user = ndb.Key(urlsafe=user_key).get()
        except ProtocolBufferDecodeError, e:
            logging.warn('Invalid user key')
        return user

