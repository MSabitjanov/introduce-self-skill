from mycroft import MycroftSkill, intent_file_handler


class IntroduceSelf(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('self.introduce.intent')
    def handle_self_introduce(self, message):
        self.speak_dialog('self.introduce')

    @intent_file_handler('who.created.you.intent')
    def handle_who_created_you(self, message):
        self.speak_dialog('who.created.you')

    @intent_file_handler('change.voice.intent')
    def handle_change_voice(self, message):
        self.speak_dialog('change.voice')

def create_skill():
    return IntroduceSelf()

