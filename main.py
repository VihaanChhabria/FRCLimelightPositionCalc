import math

# Function to convert inches to meters
def inchesToMeters(inch: float) -> float:
    return inch / 39.37

# Function to convert degrees to radians
def degToRad(deg: float) -> float:
    return deg * (math.pi / 180)

def translatePose(originalPose:dict[str, float], degreesRotate: float, distance: float) -> dict[str, float]:
    newXCoord: float = originalPose["x"] + (math.cos(degToRad(degreesRotate)) * distance)
    newYCoord: float = originalPose["y"] + (math.sin(degToRad(degreesRotate)) * distance)

    return {"x": newXCoord, "y": newYCoord, "rotation": originalPose['rotation']}

# Dictionary to hold the positions of the April tags
TAG_POSES = {
    1: {'x': inchesToMeters(657.37), 'y': inchesToMeters(25.8), 'rotation': degToRad(126)},
    2: {'x': inchesToMeters(657.37), 'y': inchesToMeters(291.2), 'rotation': degToRad(234)},
    3: {'x': inchesToMeters(455.15), 'y': inchesToMeters(317.15), 'rotation': degToRad(270)},
    4: {'x': inchesToMeters(365.2), 'y': inchesToMeters(241.64), 'rotation': degToRad(0)},
    5: {'x': inchesToMeters(365.2), 'y': inchesToMeters(75.39), 'rotation': degToRad(0)},
    6: {'x': inchesToMeters(530.49), 'y': inchesToMeters(130.17), 'rotation': degToRad(300)},
    7: {'x': inchesToMeters(546.87), 'y': inchesToMeters(158.5), 'rotation': degToRad(0)},
    8: {'x': inchesToMeters(530.49), 'y': inchesToMeters(186.83), 'rotation': degToRad(60)},
    9: {'x': inchesToMeters(497.77), 'y': inchesToMeters(186.83), 'rotation': degToRad(120)},
    10: {'x': inchesToMeters(481.39), 'y': inchesToMeters(158.5), 'rotation': degToRad(180)},
    11: {'x': inchesToMeters(497.77), 'y': inchesToMeters(130.17), 'rotation': degToRad(240)},
    12: {'x': inchesToMeters(33.51), 'y': inchesToMeters(25.8), 'rotation': degToRad(54)},
    13: {'x': inchesToMeters(33.51), 'y': inchesToMeters(291.2), 'rotation': degToRad(306)},
    14: {'x': inchesToMeters(325.68), 'y': inchesToMeters(241.64), 'rotation': degToRad(180)},
    15: {'x': inchesToMeters(325.68), 'y': inchesToMeters(75.39), 'rotation': degToRad(180)},
    16: {'x': inchesToMeters(235.73), 'y': inchesToMeters(-0.15), 'rotation': degToRad(90)},
    17: {'x': inchesToMeters(160.39), 'y': inchesToMeters(130.17), 'rotation': degToRad(240)},
    18: {'x': inchesToMeters(144), 'y': inchesToMeters(158.5), 'rotation': degToRad(180)},
    19: {'x': inchesToMeters(160.39), 'y': inchesToMeters(186.83), 'rotation': degToRad(120)},
    20: {'x': inchesToMeters(193.1), 'y': inchesToMeters(186.83), 'rotation': degToRad(60)},
    21: {'x': inchesToMeters(209.49), 'y': inchesToMeters(158.5), 'rotation': degToRad(0 + 180)},
    22: {'x': inchesToMeters(193.1), 'y': inchesToMeters(130.17), 'rotation': degToRad(300 + 180)},
}

print("Place your robot straight in front of an April tag about 1-2 meters away. You want your limelight to see the April tag.")
tagID: int = int(input("What April tag ID are you using?: "))
realDistanceFromTag: float = float(input("How far away is the robot center (m): "))
limelightPoseX: float = float(input("What is the X value that the limelight thinks the robot is? (m): "))
limelightPoseY: float = float(input("What is the Y value that the limelight thinks the robot is? (m): "))
limelightPoseRotation: float = float(input("What is the rotation value that the limelight thinks the robot is? (rad): "))

realPose: dict[str, float] = translatePose(TAG_POSES[tagID], TAG_POSES[tagID]["rotation"], realDistanceFromTag / 2)

offsetX: float = limelightPoseX-realPose['x']
offsetY: float = limelightPoseY-realPose['y']
offsetRotation: float = limelightPoseRotation-realPose['rotation']

print("Offset X: ", offsetX)
print("Offset Y: ", offsetY)
print("Offset Rotation: ", offsetRotation)