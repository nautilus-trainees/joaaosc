# Base oficial do ROS 2 Jazzy. O Docker escolhe sozinho a versão certa para arm64 ou x86-64.
FROM ros:jazzy-ros-base

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential git python3-colcon-common-extensions python3-vcstool \
    && rm -rf /var/lib/apt/lists/*

# Todo terminal interativo carrega o ROS 2 e, se já existir, o workspace compilado em /workspace.
RUN echo 'source /opt/ros/jazzy/setup.bash' >> /root/.bashrc \
    && echo '[ -f /workspace/install/setup.bash ] && source /workspace/install/setup.bash' >> /root/.bashrc

# "colcon build" passa a usar --symlink-install: editar um arquivo Python dispensa recompilar.
RUN mkdir -p /root/.colcon \
    && printf 'build:\n  symlink-install: true\n' > /root/.colcon/defaults.yaml

WORKDIR /workspace
