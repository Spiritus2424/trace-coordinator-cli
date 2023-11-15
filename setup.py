from setuptools import setup


setup(
    name='trace-coordinator-cli',
    version='1.0.0',
    entry_points={
        'console_scripts': [
            'trace-coordinator=trace_coordinator_cli:cli',
        ],
    },   
)