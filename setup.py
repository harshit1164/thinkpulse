from setuptools import setup, find_packages

setup(
    name="thinkpulse",
    version="0.1",
    description="The simplest, fastest, and bilingual data science toolkit",
    author="Harshit Tiwari",
    author_email="tiwariharshit1164@gmail.com",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "scipy"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    python_requires=">=3.7",
)
