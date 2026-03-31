#!/usr/bin/env python3

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    
    # Объявляем аргументы launch-файла
    rate_arg = DeclareLaunchArgument(
        'rate',
        default_value='2.0',
        description='Частота публикации температуры (Гц)'
    )
    
    warning_temp_arg = DeclareLaunchArgument(
        'warning_temp',
        default_value='35.0',
        description='Порог предупреждения (°C)'
    )
    
    critical_temp_arg = DeclareLaunchArgument(
        'critical_temp',
        default_value='40.0',
        description='Критический порог температуры (°C)'
    )
    
    mode_arg = DeclareLaunchArgument(
        'mode',
        default_value='normal',
        description='Режим работы: normal или test'
    )
    
    # Получаем значения аргументов
    rate = LaunchConfiguration('rate')
    warning_temp = LaunchConfiguration('warning_temp')
    critical_temp = LaunchConfiguration('critical_temp')
    mode = LaunchConfiguration('mode')
    
    # Логика для режима test
    # Используем Python выражения для модификации параметров
    def get_parameters():
        # Здесь мы вернём словарь с параметрами,
        # но в LaunchConfiguration нельзя напрямую использовать if
        
        # Вместо этого создадим узлы с разными параметрами в зависимости от режима
        pass
    
    # Создаём узлы с возможностью переопределения через аргументы
    # Для режима test будем использовать переопределение через командную строку
    
    # Узел temperature_sensor
    # Параметры будут взяты из LaunchConfiguration
    # Режим test обрабатывается через переопределение аргументов при запуске
    
    sensor_node = Node(
        package='super_Maxim_study_pkg',
        executable='temperature_sensor',
        name='temp_sensor',
        output='screen',
        parameters=[{
            'publish_rate': rate,
            'min_temp': 15.0,      # фиксированные значения
            'max_temp': 45.0,      # фиксированные значения
            'sensor_name': 'main_sensor'
        }],
        # Добавляем эмуляцию режима test через условную логику
        # В реальности пользователь передаст rate:=4.0 при запуске
    )
    
    # Узел temperature_monitor
    monitor_node = Node(
        package='super_Maxim_study_pkg',
        executable='temperature_monitor',
        name='temp_monitor',
        output='screen',
        parameters=[{
            'warning_threshold': warning_temp,
            'critical_threshold': critical_temp
        }]
    )
    
    # Добавляем информативное сообщение о режиме работы
    from launch.actions import LogInfo
    from launch.substitutions import TextSubstitution
    
    mode_info = LogInfo(
        msg=['Запуск системы мониторинга температуры в режиме: ', mode]
    )
    
    return LaunchDescription([
        rate_arg,
        warning_temp_arg,
        critical_temp_arg,
        mode_arg,
        mode_info,
        sensor_node,
        monitor_node,
    ])