import random
from server import ServerMessageTypes, ServerComms

class Movement:

    def __init__(self, GameServer):
        self.GameServer = GameServer

    def turn(self,message,):
        self.GameServer.sendMessage(ServerMessageTypes.TURNTOHEADING, {
            'Amount': random.randint(0, 359)}) # random turning

    def moveforward(self,message):
        self.GameServer.sendMessage(ServerMessageTypes.MOVEFORWARDDISTANCE, {
            'Amount': random.randint(0,10)}) # random moving forward

    def movebackward(self,message):
        self.GameServer.sendMessage(ServerMessageTypes.MOVEBACKWARDDISTANCE, {
            'Amount': random.randint(0,10)}) # random moving backward
