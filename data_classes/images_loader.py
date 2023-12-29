from data_classes.image_question import ImageQuestion
from models.ianswer import Answer
from models.iloader import ILoader
from models.iquestion import IQuestion
from models.singleton import Singleton

import random


class ImagesLoader(ILoader):
    def load(self):
        with open("data/data.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()

            for i, line in enumerate(lines):
                line = line.strip()
                answer = Answer(line)
                self._questions.append(ImageQuestion([answer], answer, f"data/{i}.jpg"))

    def save(self, data):
        raise NotImplementedError

    def get_answers(self):
        correct_answer = self._current_question.correct_answer
        answers = [correct_answer]

        while len(answers) < 4:
            answer = random.choice(self._questions).correct_answer
            if answer not in answers:
                answers.append(answer)

        random.shuffle(answers)
        return answers


