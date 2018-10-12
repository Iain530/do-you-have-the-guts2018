from server import ServerMessageTypes
import logging


class Attacking:
    def __init__(self, GameServer, Status) -> None:
        self.status = Status
        self.GameServer = GameServer

    def fire(self):
        self.GameServer.sendMessage(ServerMessageTypes.FIRE)
        logging.info(f"Firing at heading {self.status.heading} from {self.status.position}")

    
