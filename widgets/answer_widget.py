from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.widget import Widget

from models.ianswer import Answer


Builder.load_file("widgets_kivy/answer_widget.kv")


class AnswerWidget(RelativeLayout):
    text = StringProperty()
    answer: Answer
    is_marked = False

    def __init__(self, answer: Answer, on_press, **kwargs):
        super().__init__(**kwargs)
        self.answer = answer
        self.text = answer.text
        self.on_press = lambda: on_press(self)
        self.is_marked = False

    def set_marked_color(self):
        self.ids.label.text_color = (1, 1, 0, 1)
        self.is_marked = True

    def set_default_color(self):
        self.ids.label.text_color = (1, 1, 1, 1)
        self.is_marked = False

    def set_wrong_color(self):
        self.ids.label.text_color = (1, 0, 0, 1)
        self.is_marked = False

    def set_correct_color(self):
        self.ids.label.text_color = (0, 1, 0, 1)
        self.is_marked = False
