from .state import State
from .constants import COLLECTABLE_CHECKPOINTS
from utils import closest_point


class CollectHealthState(State):
    def perform(self) -> None:
        if self.closest_health is not None:
            self.body_controls.movetopoint(self.closest_health.position)
        else:
            self.body_controls.movetopoint(
                closest_point(self.status.position, COLLECTABLE_CHECKPOINTS)
            )

    def calculate_priority(self, is_current_state: bool) -> None:
        self.closest_health = self.status.find_nearest_health()
        if self.status.health == 5 or self.closest_health is None:
            return 0.02
        return (0.6 - (self.status.health * 0.1)) + (2 * 0.125)
