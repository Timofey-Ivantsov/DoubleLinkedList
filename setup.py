import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="DoubleLinkedList", 
    version="1.0.4",
    author="Ivantsov Timofey",
    author_email="TimofeyIvantsov@yandex.ru",
    description="This package is double linked list",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Timofey-Ivantsov",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.0",
)