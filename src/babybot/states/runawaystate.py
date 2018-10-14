from .state import State
from utils import within_degrees


class RunAwayState(State):
    def perform(self):
        baby_pos = self.status.position
        seentanks = self.status.recently_seen_tanks(1.5)
        for tank in seentanks:
            aimingatbabybot = tank.is_aiming_at(baby_pos)
            if aimingatbabybot == True:
                bodymovement.turntoheading(15)
                bodymovement.moveforwarddistance(5)
            else:
                return

    def calculate_priority(self, is_current_state: bool):
        if within_degrees:
            return 1
        return 0
