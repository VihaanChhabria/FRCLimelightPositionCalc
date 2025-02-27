# Limelight Offset Calibration Script

## Description
This Python script helps determine the positional offsets of a robot using a Limelight camera when tracking AprilTags. The script calculates the difference between the robot's actual position and the position estimated by the Limelight, allowing for accurate pose adjustments in FRC (FIRST Robotics Competition) applications.

## How It Works
1. The script maintains a dictionary of pre-defined AprilTag positions based on the field layout.
2. The user inputs the AprilTag ID, the real distance of the robot from the tag, and the Limelight's estimated X, Y, and rotation values.
3. The script calculates the actual robot position relative to the AprilTag using trigonometry.
4. It then computes the difference (offset) between the Limelight's estimated position and the calculated real position.
5. The script outputs these offsets, which can be used to correct the Limelight's reported position.

## Usage Instructions
1. Run the script in a Python environment.
2. Follow the prompts to input:
   - The AprilTag ID you are using.
   - The real distance from the robot's center to the tag (in meters).
   - The X, Y, and rotation values reported by the Limelight.
3. The script will output the X, Y, and rotation offsets.
4. Use these offsets in your robot code to refine pose estimation.

