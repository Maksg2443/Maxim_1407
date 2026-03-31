#!/usr/bin/env python3
import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, TextSubstitution
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    package_share_dir = get_package_share_directory('Maxim_1407')

    # --- 1. ОБЪЯВЛЯЕМ АРГУМЕНТ 'mode' ---
    # Этот аргумент можно будет передать из командной строки
    mode_arg = DeclareLaunchArgument(
        'mode',                          # имя аргумента
        default_value='slow',             # значение по умолчанию
        description='Режим работы: fast (20 Гц, порог 50) или slow (5 Гц, порог 150)'
    )

    # --- 2. ПОЛУЧАЕМ ЗНАЧЕНИЕ АРГУМЕНТА ---
    # LaunchConfiguration - это специальный объект, который позже станет строкой
    mode = LaunchConfiguration('mode')

    # --- 3. ОПРЕДЕЛЯЕМ ПУТИ К ФАЙЛАМ ПАРАМЕТРОВ ДЛЯ РАЗНЫХ РЕЖИМОВ ---
    # Мы создадим два разных YAML-файла и выберем нужный в зависимости от mode
    fast_param_file = os.path.join(package_share_dir, 'params', 'fast_params.yaml')
    slow_param_file = os.path.join(package_share_dir, 'params', 'slow_params.yaml')


    # Создаем два узла, но с условиями запуска
    from launch.conditions import IfCondition, UnlessCondition
    from launch.substitutions import PythonExpression
    
    # Вычисляем булевы значения для условий
    is_fast = PythonExpression(['"', mode, '" == "fast"'])
    is_slow = PythonExpression(['"', mode, '" == "slow"'])

    node_fast = Node(
        package='Maxim_1407',
        executable='even_pub',
        name='even_pub',
        output='screen',
        parameters=[fast_param_file],
        condition=IfCondition(is_fast)  # запустится, только если mode == 'fast'
    )

    node_slow = Node(
        package='Maxim_1407',
        executable='even_pub',
        name='even_pub',
        output='screen',
        parameters=[slow_param_file],
        condition=IfCondition(is_slow)  # запустится, только если mode == 'slow'
    )

    # Узел слушателя всегда запускается
    listener_node = Node(
        package='Maxim_1407',
        executable='overflow_listener',
        name='overflow_listener',
        output='screen',
    )

    return LaunchDescription([
        mode_arg,
        node_fast,
        node_slow,
        listener_node,
    ])
