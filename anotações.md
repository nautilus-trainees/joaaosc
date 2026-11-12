# ordem para lembrar-se sempre:
`colcon build --packages-select <pacotes>`
`source install/setup.bash` para carregar as novas intruções depois do build
`ros2 run <pacote> py_node` (o nome py_node é configurado em `setup.py`

## Comandos do Apple Container/Docker
container system start
cd "$HOME/Pesquisa/Nautilus/ambiente-v1/containers"     
    ./tools/compose/bin/compose up --pull never -f compose.dockerfile.yaml

container ls

*entrando no container:* container exec -it nautilus-ros-built bash

