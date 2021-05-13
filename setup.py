from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="edagames_grpc",
    version='1.1.0',
    description='Interface for gRPC communication',
    package_dir={'': 'src'},
    packages=find_packages(where="src"),
    python_requires='>=3.6',

    url='https://github.com/evbeda/edagames-grpc',
    author='Platform Team - EDA 5',
    author_email='ecrespillo@eventbrite.com',

    # requirements
    install_requires=[
        "grpcio==1.37.0",
        "protobuf==3.15.8",
    ],

    # LICENSE
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Environment :: Console",
        'Intended Audience :: Developers',
    ],

    # README.md
    long_description=long_description,
    long_description_content_type="text/markdown",
)
