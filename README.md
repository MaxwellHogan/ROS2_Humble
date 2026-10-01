# ROS 2 Humble Docker Teaching Environment

This repository contains the files used for the **ROS 2 Humble in Docker** teaching session. It provides a reproducible Ubuntu/ROS 2 development environment for Windows and macOS using Docker Desktop.

## Repository structure

```text
ROS2_Humble/
├── datasets/
├── docker/
│   └── Dockerfile
├── scripts/
│   ├── run_container.bat
│   ├── run_container.sh
│   └── webcam_demo.py
└── workspaces/
    └── dev_workspace/
        └── scripts/
            └── webcam_publisher.py
```

## Prerequisites

- Docker Desktop
- Visual Studio Code is recommended
- Windows GUI applications: VcXsrv/XLaunch
- macOS GUI applications: XQuartz

For macOS, enable **Allow connections from network clients** in XQuartz settings before starting the container.

## Build the Docker image

From the root of the repository:

```bash
docker build -t ros2_humble_dev -f docker/Dockerfile .
```

## Run the container

### Windows

From PowerShell or Command Prompt:

```powershell
./scripts/run_container.bat
```

### macOS

Make the script executable the first time:

```bash
chmod +x ./scripts/run_container.sh
```

Then run:

```bash
./scripts/run_container.sh
```

The launch scripts mount `workspaces/dev_workspace` into the container as `/ros2_ws`.

## Test the ROS 2 environment

Launch RViz:

```bash
rviz2
```

Launch turtlesim:

```bash
ros2 run turtlesim turtlesim_node
```

In a second terminal attached to the running container:

```bash
docker exec -it ros2_dev_container bash
ros2 run turtlesim turtle_teleop_key
```

Use the arrow keys in the teleoperation terminal to control the turtle.

## Windows webcam demonstration

The repository also contains a Windows webcam demonstration.

- `scripts/webcam_demo.py` captures the host webcam and exposes the video stream to the Docker container.
- `workspaces/dev_workspace/scripts/webcam_publisher.py` reads the stream inside the ROS 2 environment and publishes it as a ROS image topic.

The webcam demonstration is intended for the teaching demonstration and is not required for the basic Docker/ROS 2 setup.

## Notes

ROS 2 Humble is used throughout this repository. Packages installed interactively inside the container will be lost when the container is removed, so permanent dependencies should be added to the Dockerfile and the image rebuilt.
