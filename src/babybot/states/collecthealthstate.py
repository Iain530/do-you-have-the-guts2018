class CollectHealthState:
    def perform(self) -> None:
        closest_health = self.status.find_nearest_health()
        self.body_controls.move_to_point(closest_health.position)

    def calculate_priority(self, is_current_state: bool) -> None:
        return 0  # TODO
