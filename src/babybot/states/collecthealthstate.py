from .state import State


class CollectHealthState(State):
    def perform(self) -> None:
        closest_health = self.status.find_nearest_health()
        self.body_controls.move_to_point(closest_health.position)

    def calculate_priority(self, is_current_state: bool) -> None:
        if self.status.health == 5:
            return 0
        return (0.6 - (self.status.health * 0.1)) + (3 * 0.125)
