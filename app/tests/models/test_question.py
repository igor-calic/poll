from ferrisnose import AppEngineTest
from google.appengine.ext import ndb

from app.models.answer import Answer
from app.models.question import Question


class QuestionTests(AppEngineTest):

    def test_create_question(self):
        key = Question.create(text="This is question 1", order=1)
        print 'key:{0}'.format(key)
        self.assertEquals(1, Question.query().count())

    def test_sort_order(self):
        Question.create(text="This is question 1", order=2)
        Question.create(text="This is question 2", order=1)

        questions = Question.all()

        self.assertEquals(1, questions[0].order)
        self.assertEquals(2, questions[1].order)



