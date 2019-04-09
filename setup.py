import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="parsing-yandex",
    version="0.0.1",
    author="Tabakov Vlad",
    author_email="vl.tab.kov@gmail.com",
    description="package for parsing har files from yandex maps to get data on routes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
