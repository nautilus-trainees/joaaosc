from setuptools import find_packages, setup

package_name = 'meu_pacote'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='joaaosc',
    maintainer_email='86691551+joaaosc@users.noreply.github.com',
    description='TODO: Package description',
    license='MIT-0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'py_node = meu_pacote.node1:main',
        ],
    },
)
