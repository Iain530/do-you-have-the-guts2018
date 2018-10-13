from status import Status
from server import Message
from bodymovement import BodyMovement
from turretmovement import TurretMovement
import logging
from states import (DummyState, GoToGoalState, CollectHealthState, CollectAmmoState)

AVAILABLE_TURRET_STATES = [
    DummyState,
]
AVAILABLE_BODY_STATES = [
    DummyState,
    GoToGoalState,
    CollectAmmoState,
    CollectHealthState,
]


class StateMachine:
    def __init__(self, GameServer, name) -> None:
        self.status = Status(name=name)
        self.GameServer = GameServer
        self.turret_controls = TurretMovement(GameServer=GameServer, status=self.status)
        self.body_controls = BodyMovement(GameServer=GameServer, status=self.status)
        self.turret_states = list(map(
            lambda State: State(self.turret_controls, self.body_controls, self.status),
            AVAILABLE_TURRET_STATES
        ))
        self.body_states = list(map(
            lambda State: State(self.turret_controls, self.body_controls, self.status),
            AVAILABLE_BODY_STATES
        ))
        self.current_turret_state_i = 0
        self.current_turret_state = self.turret_states[0]
        self.current_body_state_i = 0
        self.current_body_state = self.body_states[0]

    def update(self, message: Message) -> None:
        self.status.update(message=message)

    def choose_state(self) -> None:
        body_priorities = [
            self.body_states[i].calculate_priority(
                self.status, i == self.current_body_state_i
            ) for i in range(len(self.body_states))
        ]
        turret_priorities = [
            self.turret_states[i].calculate_priority(
                self.status, i == self.current_turret_state_i
            ) for i in range(len(self.turret_states))
        ]
        self.current_body_state_i = body_priorities.index(max(body_priorities))
        self.current_turret_state_i = turret_priorities.index(max(turret_priorities))
        self.current_body_state = self.body_states[self.current_body_state_i]
        self.current_turret_state = self.turret_states[self.current_turret_state_i]

    def perform_current_state(self) -> None:
        logging.info(f"Performing states: {self.current_body_state} {self.current_turret_state}")
        self.current_body_state.perform()
        self.current_turret_state.perform()
