from .state import State
from utils import closest_point
from .constants import COLLECTABLE_CHECKPOINTS


class CollectAmmoState(State):
    def perform(self) -> None:
        if self.closest_ammo is not None:
            self.body_controls.movetopoint(self.closest_ammo.position)
        else:
            self.body_controls.movetopoint(
                closest_point(self.status.position, COLLECTABLE_CHECKPOINTS)
            )

    def calculate_priority(self, is_current_state: bool) -> None:
        self.closest_ammo = self.status.find_nearest_ammo()
        if self.status.ammo == 10 or self.closest_ammo is None:
            return 0.01
        return (0.5 - (self.status.ammo * 0.05)) + (1 * 0.125)
