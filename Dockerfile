# Base oficial do ROS 2 Jazzy. O Docker escolhe sozinho a versão certa para arm64 ou x86-64.
FROM ros:jazzy-ros-base

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential git python3-colcon-common-extensions python3-vcstool \
    && rm -rf /var/lib/apt/lists/*

# Todo terminal interativo já carrega o ROS 2.
RUN echo 'source /opt/ros/jazzy/setup.bash' >> /root/.bashrc

WORKDIR /workspace
