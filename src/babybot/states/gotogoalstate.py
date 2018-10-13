from status import Status
from .state import State


class GoToGoalState(State):
    def perform(self):
        goals = [(0, 100), (0, -100)]

        closestGoal = closest(self.status.position, goals)

        self.body_controls.movetopoint(closestGoal)

    def calculate_priority(self, status: Status, is_current_state: bool):
        return 0
