import json
import logging

from app.models.answer import Answer
from app.models.user import User
from app.models.user_answer import UserAnswer
from ferris import Controller, route_with
from ferris.core import messages


class UserAnswers(Controller):

    class Meta:
        prefixes = ('api',)
        components = (messages.Messaging, )
        Message = Answer.message()

    @route_with('/api/user/<user_key>/answers', methods=['POST'])
    def api_save_user_answers(self, user_key):
        logging.info('saving answers for {0}'.format(user_key))
        user = User.by_urlsafe_key(user_key)
        if user is not None:
            body = json.loads(self.request.body)
            logging.info('user {0}'.format(user.name))
            logging.info('answers:{0}'.format(body['answers']))
            UserAnswer.create_or_update(user.key, urlsafe_answers=body['answers'])

            return 200
        else:
            return 404

    @route_with('/api/user/<user_key>/answers', methods=['GET'])
    def api_user_answers_by_user(self, user_key):
        logging.info('getting answers for {0}'.format(user_key))
        user = User.by_urlsafe_key(user_key)
        if user is not None:
            answers = UserAnswer.by_user(user.key)
            logging.info('retrieved answers: {0}'.format(answers))
            if answers:
                self.context['data'] = answers
            else:
                return 200

    @route_with('/api/user/stats', methods=['GET'])
    def api_user_answer_stats(self):
        stats = UserAnswer.stats()
        logging.info('stats:{0}'.format(stats))
        return 200





