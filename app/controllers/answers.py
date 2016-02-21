from app.models.answer import Answer
from ferris import Controller, route_with
from ferris.core import messages


class Answers(Controller):
    class Meta:
        prefixes = ('api', )
        components = (messages.Messaging, )
        Message = Answer.message()

    @route_with('/api/answers')
    def api_all_answers(self):
        self.context['data'] = Answer.all()

