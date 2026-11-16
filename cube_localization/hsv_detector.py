import cv2
import numpy as np


# HSV colour ranges for the four target cube colours.
# OpenCV represents Hue from 0-179, and Saturation/Value from 0-255.
# These thresholds are initial estimates and will need tuning with real cubes.
HSV_RANGES = {
    "red": [
        # Red appears at both ends of the hue scale, so two ranges are needed.
        ((0, 100, 70), (10, 255, 255)),
        ((170, 100, 70), (179, 255, 255))
    ],
    "white": [
        # White has low saturation and high brightness, regardless of hue.
        ((0, 0, 180), (179, 60, 255)),
    ],
    "blue": [
        ((95, 80, 60), (135, 255, 255)),
    ],
    "green": [
        ((35, 80, 60), (85, 255, 255)),
    ],
}

# BGR colours used to draw bounding boxes around detected cubes.
# Yellow is used for white cubes so the bounding box is easier to see.
DRAW_COLORS = {
    "red": (0, 0, 255),
    "white": (0, 255, 255),
    "blue": (255, 0, 0),
    "green": (0, 255, 0),
}

