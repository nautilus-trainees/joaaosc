#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

# Template pra qualquer nó no futuro
class MyNode(Node):

    def __init__(self):
        super().__init__("py_test")
        self.counter_ = 0
        self.get_logger().info("Oi, mundo!")
        self.create_timer(1.0, self.timer_callback) # chama a função a cada 1 segundo

    def timer_callback(self):
        self.get_logger().info("Oi " + str(self.counter_))
        self.counter_ += 1


def main(args=None):
    rclpy.init(args=args) # inicia o ROS2 para comunicação
    node = MyNode() # Pega nossa classe MyNode herdada de Node
    rclpy.spin(node)
    rclpy.shutdown()
    # sobre spin: executa um loop para manter o nó vivo esperando por eventos e executando seus callbacks
    # callback: é uma função passada como argumento para outro código que será executada futuramente

if __name__ == '__main__':
    main()



