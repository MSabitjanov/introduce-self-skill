from mycroft import MycroftSkill, intent_file_handler


class IntroduceSelf(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('self.introduce.intent')
    def handle_self_introduce(self, message):
        self.speak_dialog('self.introduce')


def create_skill():
    return IntroduceSelf()

