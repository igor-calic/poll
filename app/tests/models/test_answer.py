from ferrisnose import AppEngineTest

from app.models.answer import Answer
from app.models.question import Question


class AnswerTests(AppEngineTest):

    def test_sorting_by_order(self):
        question_key = Question.create(text="Q1", order=1)
        Answer.create(question_key=question_key, text="Answer 1", value=1, order=3)
        Answer.create(question_key=question_key, text="Answer 2", value=2, order=1)
        Answer.create(question_key=question_key, text="Answer 3", value=3, order=2)

        answers = Answer.by_question(question_key)

        self.assertEquals(1, answers[0].order)
        self.assertEquals(2, answers[1].order)
        self.assertEquals(3, answers[2].order)
