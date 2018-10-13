from server import ServerMessageTypes
import logging


class TurretMovement:
    def __init__(self, GameServer, status) -> None:
        self.status = status
        self.GameServer = GameServer

    def fire(self):
        self.GameServer.sendMessage(ServerMessageTypes.FIRE)
        logging.info(f"Firing at heading {self.status.heading} from {self.status.position}")

    def aim_at_heading(self, heading: float):
        self.GameServer.sendMessage(ServerMessageTypes.TURNTURRETTOHEADING, {
            'Amount': heading
        })

    def aim_left(self):
        self.GameServer.sendMessage(ServerMessageTypes.TOGGLETURRETLEFT)

    def aim_right(self):
        self.GameServer.sendMessage(ServerMessageTypes.TOGGLETURRETRIGHT)

    def stop_turn_turret(self):
        self.GameServer.sendMessage(ServerMessageTypes.STOPTURRET)
