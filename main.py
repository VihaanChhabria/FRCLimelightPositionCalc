import math

# Function to convert inches to meters
def inchesToMeters(inch: float) -> float:
    return inch / 39.37

# Function to convert degrees to radians
def degToRad(deg: float) -> float:
    return deg * (math.pi / 180)

# Dictionary to hold the positions of the April tags
TAG_POSES = {
    1: {'x': inchesToMeters(657.37), 'y': inchesToMeters(25.8), 'rotation': degToRad(126 + 180)},
    2: {'x': inchesToMeters(657.37), 'y': inchesToMeters(291.2), 'rotation': degToRad(234 + 180)},
    3: {'x': inchesToMeters(455.15), 'y': inchesToMeters(317.15), 'rotation': degToRad(270 + 180)},
    4: {'x': inchesToMeters(365.2), 'y': inchesToMeters(241.64), 'rotation': degToRad(0 + 180)},
    5: {'x': inchesToMeters(365.2), 'y': inchesToMeters(75.39), 'rotation': degToRad(0 + 180)},
    6: {'x': inchesToMeters(530.49), 'y': inchesToMeters(130.17), 'rotation': degToRad(300 + 180)},
    7: {'x': inchesToMeters(546.87), 'y': inchesToMeters(158.5), 'rotation': degToRad(0 + 180)},
    8: {'x': inchesToMeters(530.49), 'y': inchesToMeters(186.83), 'rotation': degToRad(60 + 180)},
    9: {'x': inchesToMeters(497.77), 'y': inchesToMeters(186.83), 'rotation': degToRad(120 + 180)},
    10: {'x': inchesToMeters(481.39), 'y': inchesToMeters(158.5), 'rotation': degToRad(180 + 180)},
    11: {'x': inchesToMeters(497.77), 'y': inchesToMeters(130.17), 'rotation': degToRad(240 + 180)},
    12: {'x': inchesToMeters(33.51), 'y': inchesToMeters(25.8), 'rotation': degToRad(54 + 180)},
    13: {'x': inchesToMeters(33.51), 'y': inchesToMeters(291.2), 'rotation': degToRad(306 + 180)},
    14: {'x': inchesToMeters(325.68), 'y': inchesToMeters(241.64), 'rotation': degToRad(180 + 180)},
    15: {'x': inchesToMeters(325.68), 'y': inchesToMeters(75.39), 'rotation': degToRad(180 + 180)},
    16: {'x': inchesToMeters(235.73), 'y': inchesToMeters(-0.15), 'rotation': degToRad(90 + 180)},
    17: {'x': inchesToMeters(160.39), 'y': inchesToMeters(130.17), 'rotation': degToRad(240 + 180)},
    18: {'x': inchesToMeters(144), 'y': inchesToMeters(158.5), 'rotation': degToRad(180 + 180)},
    19: {'x': inchesToMeters(160.39), 'y': inchesToMeters(186.83), 'rotation': degToRad(120 + 180)},
    20: {'x': inchesToMeters(193.1), 'y': inchesToMeters(186.83), 'rotation': degToRad(60 + 180)},
    21: {'x': inchesToMeters(209.49), 'y': inchesToMeters(158.5), 'rotation': degToRad(0 + 180)},
    22: {'x': inchesToMeters(193.1), 'y': inchesToMeters(130.17), 'rotation': degToRad(300 + 180)},
}

print("Place your robot straight in front of an April tag about 1-2 meters away. You want your limelight to see the April tag.")
tagID: int = int(input("What April tag ID are you using?: "))
realDistanceFromTag: float = float(input("How far away is the robot (m): "))

