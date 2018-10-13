from .state import State


class CollectAmmoState(State):
    def perform(self) -> None:
        self.body_controls.movetopoint(self.closest_ammo.position)

    def calculate_priority(self, is_current_state: bool) -> None:
        self.closest_ammo = self.status.find_nearest_ammo()
        if self.status.ammo == 10 or self.closest_ammo is None:
            return 0
        return (0.5 - (self.status.ammo * 0.05)) + (1 * 0.125)
