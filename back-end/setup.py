from setuptools import setup, find_packages

setup(
    name="LLM Document Manager Demo",
    version="0.1.0",
    description="This app creates metadata provided documents and metadata descriptions",
    author="Duncan Maina",
    author_email="duncandevs@gmail.com",
    url="https://www.linkedin.com/in/duncan-maina-499677135/",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'start-app=index:start_function',
        ],
    },
)
