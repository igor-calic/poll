from app.models.question import Question, QuestionMessage
from ferris import Controller, route_with
from ferris.core import messages


class Questions(Controller):

    class Meta:
        prefixes = ('api', )
        components = (messages.Messaging, )
        Message = QuestionMessage
        messaging_transform_function = Question.to_message

    @route_with('/api/questions')
    def api_all_questions(self):
        self.context['data'] = Question.all()
