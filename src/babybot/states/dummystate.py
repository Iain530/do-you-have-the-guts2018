from .state import State


class DummyState(State):
    def perform(self):
        pass

    def calculate_priority(self, is_current_state: bool):
        return 1
