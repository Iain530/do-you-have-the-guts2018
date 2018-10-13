from .state import State
from enemy import Enemy
# from babybot import BodyMovement

class RunAwayState(State):
    def perform(self):
        baby_pos = self.status.position
        alltanks = self.status.other_tanks
        for tank in alltanks:
            aimingatbabybot = tank.is_aiming_at(baby_pos)
            if aimingatbabybot == True:
                pass

    def calculate_priority(self, is_current_state: bool):
        # if not in bullet's width, priority = 0
        # if in bullet's width, priority = 1
        pass
