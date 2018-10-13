import random
from server import ServerMessageTypes


class Movement:

    def __init__(self, GameServer, status):
        self.GameServer = GameServer
        self.moving = False
        self.turning = False
        self.status = status

    def turn(self):
        self.GameServer.sendMessage(ServerMessageTypes.TURNTOHEADING, {
            'Amount': random.randint(0, 359)}) # random turning

    def moveforwarddistance(self):
        self.GameServer.sendMessage(ServerMessageTypes.MOVEFORWARDDISTANCE, {
            'Amount': random.randint(0,10)}) # random moving forward

    def movebackwarddistance(self):
        self.GameServer.sendMessage(ServerMessageTypes.MOVEBACKWARDDISTANCE, {
            'Amount': random.randint(0,10)}) # random moving backward

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
