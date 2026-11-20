# TODO: Create the ROS 2 node and subscribe to the ZED RGB, depth, and camera info topics.

# TODO: Convert incoming ROS camera images to OpenCV BGR format
# using CvBridge, then convert BGR to HSV before passing
# the image to the HSV detector.

# TODO: Run HSV detector to identify colored cube candidates.
# TODO: Use depth data to calculate their 3D positions.
# TODO: Publish the detected cubes and their positions.