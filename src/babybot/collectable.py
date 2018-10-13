from server import ObjectUpdate
from time import time

COLLECTABLE_TYPES = set(['AmmoPickup', 'HealthPickup', 'Snitch'])


class Collectable:

    def __init__(self, payload: ObjectUpdate) -> None:
        self.name = payload.name
        self.id = payload.id
        self.type = payload.type
        self.last_seen = time()
        self.position = (payload.x, payload.y)

    def update(self, payload: ObjectUpdate) -> None:
        self.last_seen = time()
        self.position = (payload.x, payload.y)

    def time_since_last(self):
        timesincelastseen = time() - self.last_seen
        return timesincelastseen
