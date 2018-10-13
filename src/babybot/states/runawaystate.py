from .state import State
from utils import within_degrees

class RunAwayState(State):
    def perform(self):
        baby_pos = self.status.position
        alltanks = self.status.other_tanks
        for tank in alltanks:
            aimingatbabybot = tank.is_aiming_at(baby_pos)
            if aimingatbabybot == True:
                pass

    def calculate_priority(self, is_current_state: bool):
        if within_degrees:
            return 1
        return 0