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
        'grpclib',
        'click',
        'numpy',
        'tqdm'
    ],
    packages=["grpc_performance"],
    entry_points={
        'console_scripts': [
            'data_streamer_client=grpc_performance.data_streamer_client:main',
            'data_streamer_grpclib_client=grpc_performance.data_streamer_grpclib_client:main',
            'data_streamer_server=grpc_performance.data_streamer_server:main',
            'data_streamer_grpclib_server=grpc_performance.data_streamer_grpclib_server:main'
        ]
    },
    python_requires='>=3.8',
)