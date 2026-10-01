# Use the official ROS2 Humble desktop image as a base
FROM ros:humble-ros-base

# Install additional development tools (if needed)
RUN apt-get update && apt-get install -y \
    ros-humble-desktop \
    ros-humble-ros-gz \
    build-essential \
    python3-colcon-common-extensions \
    python3-pip \
    python3-opencv \
    python3-numpy \
    python3-matplotlib \
    python3-scipy \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get install ros-humble-ros-gz

RUN echo "source /opt/ros/humble/setup.bash" >> /root/.bashrc

# Set a default working directory (your ROS2 workspace)
WORKDIR /ros2_ws
