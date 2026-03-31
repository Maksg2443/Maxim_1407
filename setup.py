from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'super_Maxim_study_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
    
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),

        (os.path.join('share', package_name, 'rviz'), glob(os.path.join('rviz', '*launch.[pxy][yma]*'))),
        (os.path.join('share', package_name, 'config'), glob(os.path.join('config', '*.yaml'))),
        
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='igsp-01',
    maintainer_email='ldsp-pish@example.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'time = super_Maxim_study_pkg.time:main',
            'even_number_publisher = super_Maxim_study_pkg.even_number_publisher:main',
            'overflow_listener = super_Maxim_study_pkg.overflow_listener:main',
            'temperature_sensor = super_Maxim_study_pkg.temperature_sensor:main',
            'temperature_monitor = super_Maxim_study_pkg.temperature_monitor:main',

        ],
    },
)
