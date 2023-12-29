from abc import ABC, abstractmethod

from kivymd.uix.screen import MDScreen

from models.ianswer import Answer
from models.iloader import ILoader
from models.iquestion import IQuestion


class IScreen(MDScreen):
    def __init__(self, loader: ILoader, **kwargs):
        super().__init__(**kwargs)
        self.loader = loader

    def mark_answer(self, answer: Answer) -> None:
        self.loader.mark_answer(answer)
        