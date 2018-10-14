from .state import State
from utils import calculate_distance, heading_from_to, within_degrees


class RunAwayState(State):
    def perform(self):
        baby_pos = self.status.position
        next_heading = heading_from_to(baby_pos, self.tank.current_pos())

        # Move to side
        if within_degrees(180, self.status.heading, (next_heading + 90) % 360):
            next_heading = (next_heading + 50) % 360
        else:
            next_heading = (next_heading - 50) % 360

        self.body_controls.turntoheading(next_heading)
        self.body_controls.moveforwarddistance(5)

    def calculate_priority(self, is_current_state: bool):
        baby_pos = self.status.position
        seentanks = self.status.recently_seen_tanks(2)
        for tank in seentanks:
            in_danger = all((
                tank.is_aiming_at(baby_pos),
                tank.has_ammo(),
                calculate_distance(self.status.position, tank.current_pos()) < 35
            ))
            if in_danger:
                self.tank = tank
                return 0.75
        return 0
