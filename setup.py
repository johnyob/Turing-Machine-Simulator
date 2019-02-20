import setuptools

with open("README.md", "r") as file:
    long_description = file.read()

requires = []

packages = [
    "turing_machine",
    "turing_machine.helpers"
]

setuptools.setup(
    name="turing-machine",
    version="0.0.1",
    author="Alistair O'Brien",
    author_email="alistair@duneroot.co.uk",
    description="A simple Python Turing machine simulator with an \"infinite\" tape",
    long_description=long_description,
    include_package_data=True,
    long_description_content_type="text/markdown",
    url="https://github.com/johnyob/Turing-Machine-Simulator",
    packages=packages,
    install_requires=requires,
)
