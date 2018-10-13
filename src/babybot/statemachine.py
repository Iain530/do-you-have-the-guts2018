from status import Status
from server import Message
from bodymovement import BodyMovement
from turretmovement import TurretMovement

STATES = ['']


class StateMachine:
    def __init__(self, GameServer, name) -> None:
        self.status = Status(name=name)
        self.GameServer = GameServer
        self.turretcontrols = TurretMovement(GameServer=GameServer, status=self.status)
        self.bodycontrols = BodyMovement(GameServer=GameServer, status=self.status)
        self.current_state = STATES[0]

    def update(self, message: Message):
        pass

    def choose_state(self) -> None:
        pass
