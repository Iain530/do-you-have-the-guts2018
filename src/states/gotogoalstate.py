from .state import State
from utils import closest_point


class GoToGoalState(State):
    def perform(self):
        goals = [(0, 100), (0, -100)]

        closestGoal = closest_point(self.status.position, goals)

        self.body_controls.movetopoint(closestGoal)

    def calculate_priority(self, is_current_state: bool):
        if self.status.points == 0:
            return 0  # Even though highest priority, if no points, no action
        return (self.status.points * 0.2) + (4 * 0.125)
