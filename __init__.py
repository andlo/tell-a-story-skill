from mycroft import MycroftSkill, intent_file_handler


class TellAStory(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('story.a.tell.intent')
    def handle_story_a_tell(self, message):
        self.speak_dialog('story.a.tell')


def create_skill():
    return TellAStory()

