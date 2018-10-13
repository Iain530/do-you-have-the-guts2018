from .state import State


class RunAwayState(State):
    def perform(self):
        # run away
        pass

    def calculate_priority(self, is_current_state: bool):
        # if not in bullet's width, priority = 0
        # if in bullet's width, priority = 1
        pass
