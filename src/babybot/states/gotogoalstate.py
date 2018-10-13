from .state import State
from utils import closest_point


class GoToGoalState(State):
    def perform(self):
        goals = [(0, 100), (0, -100)]

        closestGoal = closest_point(self.status.position, goals)

        self.body_controls.movetopoint(closestGoal)

    def calculate_priority(self, is_current_state: bool):
        return 0
