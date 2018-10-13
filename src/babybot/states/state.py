from abc import ABC, abstractmethod
from status import Status

class State(ABC):

    def __init__(self, turret_controls, body_controls, status):
        this.turret_controls = turret_controls
        this.body_controls = body_controls
        this.status = status

    @abstractmethod
    def perform_action(self):
        pass

    @abstractmethod
    def calculate_priority(self, is_current_state: bool):
        pass
