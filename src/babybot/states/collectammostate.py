from .state import State


class CollectAmmoState(State):
    def perform(self) -> None:
        closest_ammo = self.status.find_nearest_ammo()
        self.body_controls.movetopoint(closest_ammo.position)

    def calculate_priority(self, is_current_state: bool) -> None:
        if self.status.ammo == 10:
            return 0
        return (0.5 - (self.status.ammo * 0.05)) + (1 * 0.125)
