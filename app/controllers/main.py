import logging

from app.models.answer import Answer
from app.models.question import Question
from app.models.user import User
from ferris import Controller, route_with


class Main(Controller):

    @route_with('/')
    def index(self):
        self.context['user'] = 'none'

    @route_with('/:<user_key>')
    def index_with_key(self, user_key):
        user = User.by_urlsafe_key(user_key)
        logging.info('user:{0}'.format(user))
        if user is None:
            self.context['user'] = 'none'
        else:
            self.context['user'] = user.name
            self.context['userKey'] = user.key.urlsafe()

    @route_with('/api/init')
    def init(self):
        Question.clear()
        Answer.clear()

        q1 = Question.create(text="Preferred date", order=1)
        Answer.create(question_key=q1, text="Thu 18/02", order=1, value=1)
        Answer.create(question_key=q1, text="Fri 19/02", order=2, value=2)
        Answer.create(question_key=q1, text="Sat 20/02", order=3, value=3)
        Answer.create(question_key=q1, text="Sun 21/02", order=4, value=4)
        Answer.create(question_key=q1, text="Mon 22/02", order=5, value=5)
        Answer.create(question_key=q1, text="Tue 23/02", order=6, value=6)
        Answer.create(question_key=q1, text="Wed 24/02", order=7, value=7)
        Answer.create(question_key=q1, text="Thu 25/02", order=8, value=8)
        Answer.create(question_key=q1, text="Fri 26/02", order=9, value=9)

        q2 = Question.create(text="Preferred place", order=2)
        Answer.create(question_key=q2, text="Reading", order=1, value=1)
        Answer.create(question_key=q2, text="Staines", order=2, value=2)
        Answer.create(question_key=q2, text="London", order=3, value=3)

        User.create('Igor')
        User.create('Justin')
        User.create('Michael')
        User.create('Adam')
        User.create('Victor')
        User.create('Yargi')
        User.create('Varun')

        return 200
