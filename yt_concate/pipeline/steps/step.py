from abc import ABC
from abc import abstractmethod


class Step(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def process(self, data, inputs):
        pass
    # 介面更動極其危險，很容易更動到其他 Subpackage


class StepException(Exception):
    pass
