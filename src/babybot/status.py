class Status:
    def __init__(self) -> None:
        self.id = None
        self.position = (0, 0)
        self.heading = 0
        self.turret_heading = 0
        self.health = 5
        self.ammo = 10
        self.points = 0

    def update(self, message):
        pass
