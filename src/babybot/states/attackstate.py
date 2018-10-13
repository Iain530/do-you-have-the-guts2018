from .state import State
from utils import heading_from_to, within_degrees


class AttackState(State):
    def __init__(self, turret_controls, body_controls, status):
        super().__init__(turret_controls, body_controls, status)
        self.target = None

    def perform(self):
        enemy = self.target if self.target else self.status.find_nearest_enemy()
        position = self.status.position

        next_heading = heading_from_to(position, enemy.position)
        self.turret_controls.aim_at_heading(next_heading)

        heading = self.status.heading
        if within_degrees(2, heading, next_heading):
            self.turret_controls.fire()

    def calculate_priority(self, is_current_state: bool) -> float:
        return 0.5 # Default as only 2 attacking priorities
