import logging

from google.appengine.ext import ndb

from app.models.answer import AnswerMessage, Answer
from ferris import BasicModel
from ferris.core import messages


class Question(BasicModel):
    text = ndb.StringProperty(indexed=True, required=True)
    order = ndb.IntegerProperty(indexed=True, required=True)

    def __cmp__(self, other):
        return self.order.__cmp__(other.order)

    @classmethod
    def create(cls, text, order):
        question = Question(text=text, order=order)
        return question.put()

    @classmethod
    def all(cls):
        return Question.query().order(Question.order).fetch()

    @classmethod
    def clear(cls):
        while Question.query().count() > 0:
            ndb.delete_multi(Question.query().fetch(keys_only=True))

    @classmethod
    def to_message(cls, entity, message_class):
        message = QuestionMessage(key=entity.key.urlsafe(), text=entity.text, order=entity.order, answers=[])
        answers = Answer.by_question(entity.key)
        for answer in answers:
            message.answers.append(AnswerMessage(key=answer.key.urlsafe(), text=answer.text, order=answer.order, value=answer.value))
        return message


class QuestionMessage(messages.Message):
    key = messages.StringField(1)
    text = messages.StringField(2)
    order = messages.IntegerField(3)
    answers = messages.MessageField(AnswerMessage, 4, repeated=True)
