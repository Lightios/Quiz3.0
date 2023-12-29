from abc import ABC, abstractmethod
from models.ianswer import Answer


class IQuestion(ABC):
    answers: list[Answer]
    correct_answer: Answer
    label: str

    def __init__(self, answers: list[Answer], correct_answer: Answer, label: str):
        self.answers = answers
        self.correct_answer = correct_answer
        self.label = label

    def get_label(self) -> str:
        return self.label

    def get_answers(self) -> list[Answer]:
        return self.answers
