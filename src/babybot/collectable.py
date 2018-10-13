from server import ObjectUpdate
from time import time

COLLECTABLE_TYPES = set(['Ammo', ''])  # TODO


class Collectable:

    def __init__(self, payload: ObjectUpdate) -> None:
        self.name = payload.name
        self.id = payload.id
        self.type = payload.type
        self.last_seen = time()
        self.position = (payload.x, payload.y)

    def lastseentime(self):
        # if self.type == "AmmoPickup":
        #     print("Ammo. Time seen: " + self.last_seen)
        # elif self.type == "HealthPickup":
        #     print ("Health. Time seen: " + self.last_seen)
        # elif self.type == "Snitch":
        #     print("Snitch. Time seen : " + self.last_seen)

        timesincelastseen = time() - self.last_seen
        return timesincelastseen



