from abc import ABC, abstractmethod
from status import Status

class State(ABC):

    @abstractmethod
    def perform_action(self):
        pass

    @abstractmethod
    def calculate_priority(self, status: Status):
        pass
