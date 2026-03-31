import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random

class TemperatureSensor(Node):
    def __init__(self):
        super().__init__('temperature_sensor')
        
        # Объявляем параметры с значениями по умолчанию
        self.declare_parameter('publish_rate', 2.0)      # Гц
        self.declare_parameter('min_temp', 15.0)         # °C
        self.declare_parameter('max_temp', 45.0)         # °C
   
        # Читаем параметры
        self.rate = self.get_parameter('publish_rate').value
        self.min_temp = self.get_parameter('min_temp').value
        self.max_temp = self.get_parameter('max_temp').value
        
        
        # Создаём publisher
        self.publisher = self.create_publisher(Float32, '/temperature', 10)
        
        # Создаём таймер с указанной частотой
        timer_period = 1.0 / self.rate
        self.timer = self.create_timer(timer_period, self.timer_callback)
        
        
        self.get_logger().info(f'  - Частота публикации: {self.rate} Гц')
        self.get_logger().info(f'  - Диапазон температур: {self.min_temp}°C - {self.max_temp}°C')
    
    def timer_callback(self):
        # Генерируем случайную температуру в заданном диапазоне
        temperature = random.uniform(self.min_temp, self.max_temp)
        
        # Создаём сообщение
        msg = Float32()
        msg.data = temperature
        
        # Публикуем
        self.publisher.publish(msg)
        
        # Логируем
        self.get_logger().debug(f'Опубликована температура: {temperature:.2f}°C')

def main(args=None):
    rclpy.init(args=args)
    node = TemperatureSensor()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()