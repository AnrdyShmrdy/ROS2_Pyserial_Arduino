from setuptools import setup

package_name = 'serial_subscriber'

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
    maintainer='Andy Ponce',
    maintainer_email='andy.ponce@outlook.com',
    description='serial subscriber node',
    license='Apache 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
                'subscriber = serial_subscriber.serial_subscriber:main',
        ],
    },
)
