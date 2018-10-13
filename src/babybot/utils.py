from typing import Tuple
import math

Vector = Tuple[float, float]


def heading_from_to(p1: Vector, p2: Vector) -> float:
    """
    Returns the heading in degrees from point 1 to point 2
    """
    pass


def should_turn_left(current_heading: float, goal_heading: float) -> bool:
    """
    Returns true if the tank should turn left to aim at the goal
    heading.
    """
    pass

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

    return other_point

def calculate_distance(point1, point2) -> float:
    """
    Returns the distances between two points as a float
    """
    x = point2[0] - point1[0]
    y = point2[1] - point1[1]

    return (math.sqrt(x*x + y*y))
