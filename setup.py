from setuptools import setup

package_name = 'starship'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Matt Harzewski',
    maintainer_email='matt@ntugo.com',
    description='Frontier exploration for ROS2',
    license='GPL3',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'explore = starship.explore:main'
        ],
    },
)
