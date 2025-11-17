from setuptools import setup

with open('requirements.txt', encoding='utf-8') as f:
    requirements = [line.strip() for line in f if line.strip()]

setup(
    name="personal-assistant",
    version="0.1.0",
    packages=['src'],
    py_modules=['main'],
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "call-assistant=main:main",
        ],
    },
)