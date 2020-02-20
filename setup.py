
from setuptools import setup

setup(

    install_requires=[
        "emoji",
    ],

    name="demoji",
    packages=["demoji"],

    entry_points={
        "console_scripts": [
            "demoji = demoji.__main__:main",
        ],
    },

)
