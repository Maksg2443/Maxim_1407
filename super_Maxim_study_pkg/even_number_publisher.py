#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class EvenNumberPublisher(Node):

    def __init__(self):
        super().__init__('even_pub')

        # основной публикатор
        self.publisher = self.create_publisher(Int32, 'even_numbers', 10)

        # публикатор переполнения
        self.overflow_publisher = self.create_publisher(Int32, '/overflow', 10)

        # 10 Гц
        self.timer = self.create_timer(0.1, self.timer_callback)

        self.current_number = 0

        self.get_logger().info("Узел even_pub запущен!")

    def timer_callback(self):
        msg = Int32()
        msg.data = self.current_number

        # публикуем обычное число
        self.publisher.publish(msg)
        self.get_logger().info(f"Публикую: {msg.data}")

        # увеличиваем
        self.current_number += 2

        # проверка переполнения
        if self.current_number >= 100:
            overflow_msg = Int32()
            overflow_msg.data = self.current_number

            self.overflow_publisher.publish(overflow_msg)
            self.get_logger().warn(f"Переполнение! Отправлено: {overflow_msg.data}")

            # сброс
            self.current_number = 0


def main():
    rclpy.init()
    node = EvenNumberPublisher()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()