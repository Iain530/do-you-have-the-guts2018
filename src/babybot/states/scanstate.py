from .state import State
from time import time

SCAN_TIME = 1.25


class ScanState(State):
    def __init__(self, turret_controls, body_controls, status):
        super().__init__(turret_controls, body_controls, status)
        self.last_scan_time = time()
        self.scanning = False
        self.start_time = None
        self.finished_scan = False

    def perform(self):
        if not self.scanning:
            self.finished_scan = False
            self.start_time = time()
        self.turret_controls.aim_left()  # consider distance to walls?
        if time() - self.start_time > SCAN_TIME:
            self.finished_scan = True

    def calculate_priority(self, is_current_state: bool) -> float:
        if is_current_state:
            if self.finished_scan:
                self.scanning = False
                self.finished_scan = False
                self.last_scan_time = time()
            else:
                self.scanning = True
        time_since_last = time() - self.last_scan_time
        return 1 if time_since_last > 10 else 0 # Priority if it's been more than 10s since last scan
