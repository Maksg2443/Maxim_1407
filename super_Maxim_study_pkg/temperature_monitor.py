import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class TemperatureMonitor(Node):
    def __init__(self):
        super().__init__('temperature_monitor')
        
        # Объявляем параметры
        self.declare_parameter('warning_threshold', 35.0)    # °C
        self.declare_parameter('critical_threshold', 40.0)   # °C
        
        # Читаем параметры
        self.warning_threshold = self.get_parameter('warning_threshold').value
        self.critical_threshold = self.get_parameter('critical_threshold').value
        
        # Создаём подписку на топик /temperature
        self.subscription = self.create_subscription(
            Float32,
            '/temperature',
            self.temperature_callback,
            10
        )
        
        self.get_logger().info('Temperature Monitor инициализирован')
        self.get_logger().info(f'  - Порог предупреждения: {self.warning_threshold}°C')
        self.get_logger().info(f'  - Критический порог: {self.critical_threshold}°C')
    
    def temperature_callback(self, msg):
        temp = msg.data
        
        if temp > self.critical_threshold:
            self.get_logger().error(
                f'КРИТИЧЕСКАЯ ТЕМПЕРАТУРА! {temp:.2f}°C > {self.critical_threshold}°C'
            )
        elif temp > self.warning_threshold:
            self.get_logger().warn(
                f'ПРЕДУПРЕЖДЕНИЕ! Высокая температура: {temp:.2f}°C > {self.warning_threshold}°C'
            )
        else:
            self.get_logger().info(
                f'Температура в норме: {temp:.2f}°C'
            )

def main(args=None):
    rclpy.init(args=args)
    node = TemperatureMonitor()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
