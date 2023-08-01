from setuptools import setup

setup(
    name='s3_tree',
    version='0.1.0',
    url='https://github.com/selimonat/s3-tree',
    author='Selim Onat',
    author_email='onatselim@gmail.com',
    entry_points={
        'console_scripts': [
            's3-tree = s3_tree.__main__:app'
        ]
    }
)