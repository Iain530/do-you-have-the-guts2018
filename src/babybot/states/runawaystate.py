from .state import State
from utils import within_degrees, calculate_distance


class RunAwayState(State):
    def perform(self):
        baby_pos = self.status.position
        seentanks = self.status.recently_seen_tanks(1.5)
        threats = []
        for tank in seentanks:
            in_danger = all((
                tank.is_aiming_at(baby_pos),
                tank.has_ammo(),
                calculate_distance(self.status.position, tank.current_pos()) < 25
            ))
            if in_danger:
                self.bodymovement.turntoheading(15)
                self.bodymovement.moveforwarddistance(5)
                break

        if len(threats) > 0:


    def calculate_priority(self, is_current_state: bool):
        if within_degrees:
            return 1
        return 0
