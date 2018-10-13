from abc import ABC, abstractmethod
from status import Status

class GoToGoal(State):

    def perform_action(self):
        pass

    def calculate_priority(self, status: Status, is_current_state: bool):
        pass
