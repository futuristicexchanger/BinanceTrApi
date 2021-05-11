import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="BinanceTrApi",
    version="0.1.1",
    author="Futuristic Exchanger",
    author_email="futuristic.exchanger@gmail.com",
    description="TRbinance API implementation in python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["BinanceTrApi"],
    package_data = {"BinanceTrApi":["constants.json"]},
    python_requires=">=3.6",
)