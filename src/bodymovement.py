from server import ServerMessageTypes
from utils import heading_from_to
from typing import Tuple
import logging

Vector = Tuple[float, float]


class BodyMovement:
    def __init__(self, GameServer, status):
        self.GameServer = GameServer
        self.moving = False
        self.turning = False
        self.status = status

    def movetopoint(self, target: Vector):
        current_coords = self.status.position
        # get heading to turn to
        heading = heading_from_to(current_coords, target)
        # turn to heading
        self.turntoheading(heading)
        # move forwards to coords
        logging.info(f"moving toward {target}")
        if (current_coords != target):
            self.moveforwarddistance(5)

    def turntoheading(self, heading):
        self.GameServer.sendMessage(ServerMessageTypes.TURNTOHEADING, {
            'Amount': heading})

    def moveforwarddistance(self, amount):
        self.GameServer.sendMessage(ServerMessageTypes.MOVEFORWARDDISTANCE, {
            'Amount': amount})

    def movebackwarddistance(self, amount):
        self.GameServer.sendMessage(ServerMessageTypes.MOVEBACKWARDDISTANCE, {
            'Amount': amount})

    def moveforwardtoggle(self):
        self.GameServer.sendMessage(ServerMessageTypes.TOGGLEFORWARD)

    def movebackwardtoggle(self):
        self.GameServer.sendMessage(ServerMessageTypes.TOGGLEREVERSE)

    def turnlefttoggle(self):
        self.GameServer.sendMessage(ServerMessageTypes.TOGGLELEFT)

    def turnrighttoggle(self):
        self.GameServer.sendMessage(ServerMessageTypes.TOGGLERIGHT)

    def stopmoving(self):
        self.GameServer.sendMessage(ServerMessageTypes.STOPMOVE)

    def stopturning(self):
        self.GameServer.sendMessage(ServerMessageTypes.STOPTURN)
