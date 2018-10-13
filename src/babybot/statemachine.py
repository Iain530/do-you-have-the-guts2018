from status import Status
from server import Message
from bodymovement import BodyMovement
from turretmovement import TurretMovement
import logging

AVAILABLE_TURRET_STATES = []
AVAILABLE_BODY_STATES = []


class StateMachine:
    def __init__(self, GameServer, name) -> None:
        self.status = Status(name=name)
        self.GameServer = GameServer
        self.turret_controls = TurretMovement(GameServer=GameServer, status=self.status)
        self.body_controls = BodyMovement(GameServer=GameServer, status=self.status)
        self.turret_states = map(
            lambda State: State(self.turret_controls, self.body_controls, self.status),
            AVAILABLE_TURRET_STATES
        )
        self.body_states = map(
            lambda State: State(self.turret_controls, self.body_controls, self.status),
            AVAILABLE_BODY_STATES
        )
        # self.current_turrent_state_i = 0
        # self.current_turrent_state = self.turret_states[0]
        self.current_body_state_i = 0
        self.current_body_state = self.body_states[0]

    def update(self, message: Message) -> None:
        self.status.update(message=message)

    def choose_state(self) -> None:
        # body_priorities = [
        #     self.body_states[i].priority(
        #         self.status, i == self.current_body_state_i
        #     ) for i in range(len(self.body_states))
        # ]
        # turret_priorities = [
        #     self.turret_states[i].priority(
        #         self.status, i == self.current_turrent_state_i
        #     ) for i in range(len(self.turret_states))
        # ]
        pass

    def perform_current_state(self) -> None:
        logging.info(f"Performing states: {self.current_body_state}, {self.current_turrent_state}")
        self.current_body_state.perform()
        # self.current_turrent_state.perform()
