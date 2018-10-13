from .state import State
from time import time

SCAN_TIME = 1.25


class ScanState(State):
    def __init__(self, turret_controls, body_controls, status):
        super().__init__(turret_controls, body_controls, status)
        self.last_scan_time = time()
        self.scanning = True
        self.start_time = time()

    def perform(self):
        if not self.scanning:
            self.start_time = time()
            self.last_scan_time = time()
        self.turret_controls.aim_left()  # consider distance to walls?
        print(self.start_time, self.scanning)

    def calculate_priority(self, is_current_state: bool) -> float:
        if self.scanning and (time() - self.start_time) > SCAN_TIME:
            self.scanning = False
        time_since_last = time() - self.last_scan_time
        return 1 if time_since_last > 15 else 0.1 # Priority if it's been more than 10s since last scan
