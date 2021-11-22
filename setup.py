from setuptools import find_packages, setup

setup(
    name='webrobot',
    package=find_packages(include=['webrobot']),
    version='0.1',
    description='Api to control chromium browsers using puppeteer',
    author='@fernandojerez',
    license='Apache',
    install_requires=['websockets', 'pydantic', 'beautifulsoup4'],
    setup_requires=[],
    test_requires=[],
    test_suite='tests'
)
