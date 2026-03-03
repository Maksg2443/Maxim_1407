#!/usr/bin/env python3


import rclpy
from rclpy.node import Node
from datetime import datetime
rclpy.init()                   
node = Node('timer')   
def time():
    node.get_logger().info(f'Время: {datetime.now().strftime("%H:%M:%S")}')

                
timer = node.create_timer(5.0, time)
rclpy.spin(node)                        # запускаем цикл обработки
node.destroy_node()
rclpy.shutdown()

if __name__ == '__main__':
    main()
    #!/usr/bin/env python3
"""Первый узел ROS 2 — Hello World"""
