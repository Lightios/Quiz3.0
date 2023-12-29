import random
from abc import ABC, abstractmethod

from models.ianswer import Answer
from models.iquestion import IQuestion


class ILoader(ABC):
    _questions: list[IQuestion]
    _current_question: IQuestion
    _marked: Answer

    def __init__(self):
        self._questions = []
        self.load()

    @abstractmethod
    def load(self):
        pass

    def get_question(self) -> IQuestion:
        return self._current_question

    @abstractmethod
    def get_answers(self) -> list[Answer]:
        pass

    @abstractmethod
    def save(self, data):
        raise NotImplementedError

    def mark_answer(self, answer: Answer) -> None:
        self._marked = answer

    def is_correct(self) -> bool:
        return self._marked == self._current_question.correct_answer

    def get_label(self):
        return self._current_question.get_label()

    def set_new_question(self):
        self._current_question = random.choice(self._questions)
