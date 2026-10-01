#!/bin/bash

# Allow Docker containers to connect to the XQuartz X server
/opt/X11/bin/xhost +localhost

docker run -it \
    --rm \
    --name ros2_dev_container \
    -e DISPLAY=host.docker.internal:0 \
    -e QT_X11_NO_MITSHM=1 \
    -v "$HOME/ROS2_Humble/workspaces/dev_workspace:/ros2_ws" \
    ros2_humble_dev