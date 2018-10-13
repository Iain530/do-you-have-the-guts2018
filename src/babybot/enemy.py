from server import ObjectUpdate


class Enemy:
    def __init__(self, payload: ObjectUpdate) -> None:
        self.name = payload.name
        self.id = payload.id
        self.type = payload.type
        self.position = (payload.x, payload.y)
        self.heading = payload.heading
        self.turret_heading = payload.turret_heading
        self.health = payload.health
        self.ammo = payload.ammo

    def has_ammo(self) -> bool:
        return self.ammo > 0
