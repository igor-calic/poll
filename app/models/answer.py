from google.appengine.ext import ndb

from ferris import BasicModel
from ferris.core import messages


class Answer(BasicModel):
    text = ndb.StringProperty(indexed=True, required=True)
    value = ndb.IntegerProperty(indexed=True, required=True)
    order = ndb.IntegerProperty(indexed=True, required=True)

    def __cmp__(self, other):
        return self.order.__cmp__(other.order)

    @classmethod
    def create(cls, question_key, text, value, order):
        answer = Answer(parent=question_key, text=text, value=value, order=order)
        return answer.put()

    @classmethod
    def message(cls):
        return messages.model_message(Answer, only=('key', 'text', 'order', 'value'))

    @classmethod
    def clear(cls):
        while Answer.query().count() > 0:
            ndb.delete_multi(Answer.query().fetch(keys_only=True))

    @classmethod
    def by_question(cls, question_key):
        return Answer.query(ancestor=question_key).order(Answer.order).fetch()

    @classmethod
    def all(cls):
        return Answer.query().fetch()


class AnswerMessage(messages.Message):
    key = messages.StringField(1)
    text = messages.StringField(2)
    value = messages.IntegerField(3)
    order = messages.IntegerField(4)

