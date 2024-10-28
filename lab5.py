from data import Time

# Write your functions for each part in the space below.

# Part 1
   # The function for Part 1 should be within the class in data.py.


# Part 2
   # The function for Part 2 should be within the class in data.py.


# Part 3
from data import Time

def time_add(time1: Time, time2: Time) -> Time:
    new_second = (time1.second + time2.second) % 60
    extra_minute = (time1.second + time2.second) // 60
    new_minute = (time1.minute + time2.minute + extra_minute) % 60
    extra_hour = (time1.minute + time2.minute + extra_minute) // 60
    new_hour = (time1.hour + time2.hour + extra_hour) % 24
    return Time(new_hour, new_minute, new_second)

# Part 4
def is_descending(values: list[float]) -> bool:
    return all(values[i] > values[i + 1] for i in range(len(values) - 1))

# Part 5
from typing import Optional

def largest_between(numbers: list[int], lower: int, upper: int) -> Optional[int]:
    if lower > upper or not (0 <= lower < len(numbers)) or not (0 <= upper < len(numbers)):
        return None
    return max(range(lower, upper + 1), key=lambda i: numbers[i])

# Part 6
from data import Point

def furthest_from_origin(points: list[Point]) -> Optional[int]:
    if not points:
        return None
    return max(range(len(points)), key=lambda i: points[i].x**2 + points[i].y**2)
