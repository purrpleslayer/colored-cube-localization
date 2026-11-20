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

def create_color_mask(hsv_image, color):
    # Check that the requested colour is supported.
    if color not in HSV_RANGES:
        raise ValueError(f"Unsupported color: {color}")

    # Start with a black mask that matches the image dimensions.
    mask = np.zeros(hsv_image.shape[:2], dtype=np.uint8)

    # Check each HSV range for the selected colour.
    # Red has two ranges so we need to check both.
    for lower, upper in HSV_RANGES[color]:

        # Find pixels within the current HSV range.
        # Matching pixels turn white (255), while the rest stay black (0).
        range_mask = cv2.inRange(
            hsv_image,
            np.array(lower, dtype=np.uint8),
            np.array(upper, dtype=np.uint8)
        )

        # Combine the matching pixels into a single mask.
        mask = cv2.bitwise_or(mask, range_mask)

    return mask

def clean_mask(mask):
    # Use a small kernel to avoid removing distant cubes.
    kernel = np.ones((3, 3), dtype=np.uint8)

    # Remove isolated white pixels and small noisy regions.
    cleaned_mask = cv2.morphologyEx(
        mask, cv2.MORPH_OPEN, kernel
    )

    # Fill small gaps in the remaining white regions.
    cleaned_mask = cv2.morphologyEx(
        cleaned_mask, cv2.MORPH_CLOSE, kernel
    )

    return cleaned_mask
