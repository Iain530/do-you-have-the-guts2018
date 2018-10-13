import random
from server import ServerMessageTypes


class Movement:

    def __init__(self, GameServer, status):
        self.GameServer = GameServer
        self.moving = False
        self.turning = False
        self.status = status

    def turndistance(self, amount):
        self.GameServer.sendMessage(ServerMessageTypes.TURNTOHEADING, {
            'Amount': amount})

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
        if self.moving:
            self.GameServer.sendMessage(ServerMessageTypes.STOPMOVE)
        else:
            print("No move to stop.")

    def stopturning(self):
        if self.turning:
            self.GameServer.sendMessage(ServerMessageTypes.STOPTURN)
        else:
            print("No turn to stop.")
