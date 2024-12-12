from setuptools import setup

from package_test import __VERSION__, __AUTHOR__

setup(
    name='package_test',
    version=__VERSION__,
    url='https://github.com/liamheisler/package_test',
    author=__AUTHOR__,
    py_modules=['package_test'],
    install_requires=['pandas', 'numpy']
)