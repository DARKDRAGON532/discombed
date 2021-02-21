import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="discombed", 
    version="0.0.1",
    author="DARKDRAGON532",
    description="A bad discord webhooks wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/darkdragon532/discombed",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License ::  GPL-3.0 License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    install_requires=["requests"],
)