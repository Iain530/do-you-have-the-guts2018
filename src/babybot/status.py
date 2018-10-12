from message import Message
from server import ServerMessageTypes
import logging


class ObjectUpdate:
    def __init__(self, message: Message) -> None:
        self.name = message['Name']
        self.id = message['Id']
        self.type = message['Type']
        self.x = message['X']
        self.y = message['Y']
        self.heading = message['Heading']
        self.turret_heading = message['TurretHeading']
        self.health = message['Health']
        self.ammo = message['Ammo']


class Status:
    def __init__(self, name: str) -> None:
        self.name = name
        self.position = (0, 0)
        self.heading = 0
        self.turret_heading = 0
        self.health = 5
        self.ammo = 10
        self.points = 0
        self.other_tanks = dict()

    def update(self, message: Message) -> None:
        if message.type == ServerMessageTypes.OBJECTUPDATE:
            payload = ObjectUpdate(message.payload)
            if payload.name == self.name:
                self.position = (payload.x, payload.y)
                self.heading = payload.heading
                self.turret_heading = payload.turret_heading
                self.health = payload.health
                self.ammo = payload.ammo
            logging.info(self)

    def __str__(self):
        return (f"<{self.name}> Position: {self.position} Heading: {self.heading} "
                f"Turret: {self.turret_heading} Health: {self.health} Ammo: {self.ammo}")
