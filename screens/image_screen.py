from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

from models.iloader import ILoader
from models.iscreen import IScreen
from widgets.answer_widget import AnswerWidget

Builder.load_file("screens_kivy/image_screen.kv")


class ImageScreen(IScreen):
    def __init__(self, loader: ILoader, **kwargs):
        super().__init__(loader, **kwargs)

    def update_labels(self, *args):
        self.loader.set_new_question()

        self.ids.image.source = self.loader.get_label()

        self.ids.answers.clear_widgets()

        answers = self.loader.get_answers()
        for answer in answers:
            self.ids.answers.add_widget(AnswerWidget(answer, self.mark_answer))

    def on_enter(self, *args):
        self.update_labels()

    def check_answer(self):
        if self.loader.is_correct():
            for widget in self.ids.answers.children:
                if widget.is_marked:
                    widget.set_correct_color()
                else:
                    widget.set_default_color()
        else:
            for widget in self.ids.answers.children:
                if widget.is_marked:
                    widget.set_wrong_color()
                elif widget.answer == self.loader.get_question().correct_answer:
                    widget.set_correct_color()
                else:
                    widget.set_default_color()

    def mark_answer(self, answer_widget: AnswerWidget):
        self.loader.mark_answer(answer_widget.answer)

        for widget in self.ids.answers.children:
            widget.set_default_color()

        answer_widget.set_marked_color()
