from typing import Tuple
from math import atan2, pi

Vector = Tuple[float, float]


def heading_from_to(p1: Vector, p2: Vector) -> float:
    """
    Returns the heading in degrees from point 1 to point 2
    """
    x1 = p1[0]
    y1 = p1[1]

    x2 = p2[0]
    y2 = p2[1]

    angle = atan2(y2-y1, x2-x1) * (180/pi)
    angle = (angle - 360) % 360
    return abs(angle)


def should_turn_left(current_heading: float, goal_heading: float) -> bool:
    """
    Returns true if the tank should turn left to aim at the goal
    heading.
    """
    diff = goal_heading - current_heading
    if diff > 0:
        return diff > 180
    else:
        return diff >= -180
