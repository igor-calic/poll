import logging

from google.appengine.ext import ndb

from ferris import BasicModel
from ferris.core import messages


class UserAnswer(BasicModel):
    answers = ndb.KeyProperty(repeated=True)

    def answers_only(self):
        return ndb.get_multi(self.answers)

    @classmethod
    def create_or_update(cls, user_key, urlsafe_answers):
        user_answer = UserAnswer.query(ancestor=user_key).get()
        if user_answer is None:
            user_answer = UserAnswer(parent=user_key)
        answers = [ndb.Key(urlsafe=x) for x in urlsafe_answers]
        user_answer.answers = answers
        return user_answer.put()

    @classmethod
    def by_user(cls, user_key):
        answers = None
        user_answer = UserAnswer.query(ancestor=user_key).get()
        if user_answer is not None:
            answers = ndb.get_multi(user_answer.answers)
        return answers

    @classmethod
    def stats(cls):
        user_answers = UserAnswer.query().fetch()

        stats = {}

        for user_answer in user_answers:
            logging.info('getting user answer: {0}'.format(user_answer.key.urlsafe()))
            for answer_key in user_answer.answers:
                question_key = answer_key.parent()
                question_answers = stats.setdefault(question_key.urlsafe(), {})
                count = question_answers.setdefault(answer_key.urlsafe(), 0)
                question_answers[answer_key.urlsafe()] = count + 1

        msg = StatsMessage(questions=[])
        for question_key, answers in stats.iteritems():
            question_stats = QuestionStats(key=question_key, answers=[])
            for answer_key, value in answers.iteritems():
                question_stats.answers.append(AnswerStats(key=answer_key, count=value))
            msg.questions.append(question_stats)
        return msg


class AnswerStats(messages.Message):
    key = messages.StringField(1)
    count = messages.IntegerField(2)


class QuestionStats(messages.Message):
    key = messages.StringField(1)
    answers = messages.MessageField(AnswerStats, 2, repeated=True)


class StatsMessage(messages.Message):
    questions = messages.MessageField(QuestionStats, 1, repeated=True)

