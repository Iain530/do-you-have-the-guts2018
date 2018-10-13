from .state import State


class CollectHealthState(State):
    def perform(self) -> None:
        self.body_controls.movetopoint(self.closest_health.position)

    def calculate_priority(self, is_current_state: bool) -> None:
        self.closest_health = self.status.find_nearest_health()
        if self.status.health == 5 or self.closest_health is None:
            return 0
        return (0.6 - (self.status.health * 0.1)) + (3 * 0.125)
