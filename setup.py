from setuptools import setup, find_packages


setup(

    name="libscr",
    version="0.0.1",
    url="https://github.com/slacknate/libscr",
    description="A library for parsing and building BlazBlue script data.",
    packages=find_packages(include=["libscr", "libscr.*"]),
)
