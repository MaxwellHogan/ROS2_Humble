@echo on
docker run -it ^
           --rm ^
           --name ros2_dev_container ^
           -e DISPLAY=host.docker.internal:0 ^
           -v "C:\ROS2_Humble\workspaces\dev_workspace":/ros2_ws ^
           ros2_humble_dev
pause
