from .state import State
from utils import calculate_distance, heading_from_to


class RunAwayState(State):
    def perform(self):
        baby_pos = self.status.position
        next_heading = heading_from_to(baby_pos, self.tank.current_pos())

        # Move to side
        next_heading = (next_heading + 45) % 360

        self.body_controls.turntoheading(next_heading)
        self.body_controls.moveforwarddistance(5)

    def calculate_priority(self, is_current_state: bool):
        baby_pos = self.status.position
        seentanks = self.status.recently_seen_tanks(1.5)
        for tank in seentanks:
            in_danger = all((
                tank.is_aiming_at(baby_pos),
                tank.has_ammo(),
                calculate_distance(self.status.position, tank.current_pos()) < 30
            ))
            if in_danger:
                self.tank = tank
                return 1
        return 0
