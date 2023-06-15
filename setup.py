from setuptools import setup


setup(
    name='trace-coordinator-cli',
    version='1.0.0',
    entry_points={
        'console_scripts': [
            'trace-coordinator-cli=cli:main',  # command=package.module:function
        ],
    },   
)