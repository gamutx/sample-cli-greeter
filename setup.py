from setuptools import setup, find_packages

setup(
    name='greeter',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'say-hello=greeter.cli:main',
        ],
    },
    install_requires=[
        # List any dependencies here
    ],
)
