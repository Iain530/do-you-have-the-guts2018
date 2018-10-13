from .state import State


class CollectAmmoState(State):
    def perform(self) -> None:
        closest_ammo = self.status.find_nearest_ammo()
        self.body_controls.move_to_point(closest_ammo.position)

    def calculate_priority(self, is_current_state: bool) -> None:
        return 0  # TODO
