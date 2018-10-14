from typing import Tuple
import math

Vector = Tuple[float, float]


def heading_from_to(p1: Vector, p2: Vector) -> float:
    """
    Returns the heading in degrees from point 1 to point 2
    """
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]
    angle = math.atan2(y2-y1, x2-x1) * (180/math.pi)
    angle = (-angle) % 360
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


def closest_point(current_point, points) -> Vector:
    """
    Returns the point from a list of points which is closest to the given
    point.
    """
    closest = None
    distance_to_closest = math.inf

    for other_point in points:
        distance = calculate_distance(current_point, other_point)
        if (distance < distance_to_closest):
            closest = other_point
            distance_to_closest = distance
    return closest


def within_degrees(error, angle, goal):
    anglediff = (angle - goal + 180 + 360) % 360 - 180
    return - error / 2 <= anglediff <= error / 2


def calculate_distance(point1, point2) -> float:
    """
    Returns the distances between two points as a float
    """
    x = point2[0] - point1[0]
    y = point2[1] - point1[1]

    return (math.sqrt(x*x + y*y))
