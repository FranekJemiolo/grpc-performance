import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="grpc-performance",
    version="0.0.1",
    author="Franek Jemiolo",
    description="Simple grpc performance test in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FranekJemiolo/grpc-performance",
    install_requires=[
        'grpcio',
        'grpcio-tools',
        'click',
        'numpy'
    ],
    packages=["grpc_performance"],
    python_requires='>=3.7',
)