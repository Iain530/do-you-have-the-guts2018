from message import Message
from server import ServerMessageTypes, ObjectUpdate
from enemy import Enemy
from collectable import COLLECTABLE_TYPES
import logging


class Status:
    def __init__(self, name: str) -> None:
        self.name = name
        self.position = (0, 0)
        self.heading = 0
        self.turret_heading = 0
        self.health = 5
        self.ammo = 10
        self.points = 0
        self.banked_points = 0
        self.other_tanks = dict()
        self.collectables = dict()
        self.snitch_available = False
        self.snitch_carrier = None

    def update(self, message: Message) -> None:
        if message.type == ServerMessageTypes.OBJECTUPDATE:
            payload = ObjectUpdate(message.payload)
            if payload.type == 'Tank':
                if payload.name == self.name:
                    self.update_self(payload)
                else:
                    self.update_enemy(payload)
            elif payload.type in COLLECTABLE_TYPES:
                self.update_collectable(payload)
            # TODO: snitch update ?
        elif message.type == ServerMessageTypes.KILL:
            self.kill()
        elif message.type == ServerMessageTypes.ENTEREDGOAL:
            self.reached_goal()
        elif message.type == ServerMessageTypes.SNITCHAPPEARED:
            self.snitch_spawned()
        elif message.type == ServerMessageTypes.DESTROYED:
            self.respawn()
        logging.info(self)

    def kill(self) -> None:
        """ Killed an enemy """
        self.points += 1

    def reached_goal(self) -> None:
        self.banked_points += self.points
        self.points = 0

    def snitch_spawned(self) -> None:
        self.snitch_available = True

    def respawn(self) -> None:
        """ We died :( """
        self.points = 0
        self.health = 5

    def update_self(self, payload: ObjectUpdate) -> None:
        self.position = (payload.x, payload.y)
        self.heading = payload.heading
        self.turret_heading = payload.turret_heading
        self.health = payload.health
        self.ammo = payload.ammo

    def update_enemy(self, payload: ObjectUpdate) -> None:
        if payload.id not in self.other_tanks:
            self.other_tanks[id] = Enemy(payload)
        else:
            self.other_tanks[id].update(payload)

    def update_collectable(self, payload: ObjectUpdate) -> None:
        pass

    def __str__(self):
        return (f"<{self.name}> Position: {self.position} Heading: {self.heading} "
                f"Turret: {self.turret_heading} Health: {self.health} Ammo: {self.ammo}")
