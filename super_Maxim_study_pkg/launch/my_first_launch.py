
#!/usr/bin/env python3

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='Maxim_1407',           # ← замени на своё имя пакета
            executable='even_pub',
            name='even_pub',
            output='screen',
        ),
        Node(
            package='Maxim_1407',
            executable='overflow_listener',
            name='overflow_listener',
            output='screen',
        ),
    ])
