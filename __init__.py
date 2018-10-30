from mycroft import MycroftSkill, intent_file_handler
from mycroft.audio import wait_while_speaking
import io

class TellAStory(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('story.a.tell.intent')
    def handle_story_a_tell(self, message):
        self.is_reading = True
        AppPath = self._dir
        filename = AppPath + "/stories/the_little_match_girl_andersen.txt"
        with io.open(filename) as f:
            for line in f:
                if self.is_reading == False:
                    break
                wait_while_speaking()
                self.speak(line)
            self.is_reading = False

    def stop(self):
        self.is_reading = False
    
def create_skill():
    return TellAStory()

