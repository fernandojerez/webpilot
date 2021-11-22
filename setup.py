from setuptools import find_packages, setup

setup(
    name='webrobot',
    packages=find_packages(include=['webrobot']),
    version='0.1',
    description='Api to control chromium browsers using puppeteer',
    author='@fernandojerez',
    license='Apache',
    requires=['websockets', 'pydantic', 'beautifulsoup4'],
    test_suite='tests'
)
