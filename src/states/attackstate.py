from .state import State
from utils import heading_from_to, within_degrees, calculate_distance


class AttackState(State):
    def __init__(self, turret_controls, body_controls, status):
        super().__init__(turret_controls, body_controls, status)
        self.target = None

    def perform(self):
        enemy = self.target if self.target else self.status.find_best_enemy_target()
        position = self.status.position

        next_heading = heading_from_to(position, enemy.current_pos())
        # self.turret_controls.aim_left()
        self.turret_controls.aim_at_heading(next_heading)

        heading = self.status.turret_heading

        distance = calculate_distance(position, enemy.current_pos())
        angle_allowed = (105 - distance) / 5

        if within_degrees(angle_allowed, heading, next_heading):
            self.turret_controls.fire()

    def calculate_priority(self, is_current_state: bool) -> float:
        enemy = self.status.find_best_enemy_target()
        if enemy is not None and self.status.ammo > 0:
            self.target = enemy
            return 0.5  # Default as only 2 attacking priorities
        self.target = None
        return 0
