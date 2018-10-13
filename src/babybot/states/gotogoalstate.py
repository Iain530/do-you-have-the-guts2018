from abc import ABC, abstractmethod
from status import Status
from .state import State

class GoToGoalState(State):

    def perform(self):
        pass

    def calculate_priority(self, status: Status, is_current_state: bool):
        return 0
