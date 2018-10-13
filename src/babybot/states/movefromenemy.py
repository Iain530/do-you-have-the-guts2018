from .state import State
from enemy import Enemy
from babybot import BodyMovement

class MoveFromEnemy(State):
    def perform(self):
        baby_pos = self.status.position
        alltanks = self.status.other_tanks
        for tank in alltanks:
            aimingatbabybot = tank.is_aiming_at(baby_pos)
            if aimingatbabybot == True:
                

    else:
        return
