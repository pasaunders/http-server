"""Setup file for echo server assignment."""


from setuptools import setup


setup(
    name="echo",
    description="A project to build a basic echo server.",
    version=0.1,
    author="Patrick & Rick",
    author_email="patrick.a.n.saunders@gmail.com",
    license="MIT",
    py_modules=['client', 'server'],
    package_dir={'': 'src'},
    install_requires=[''],
    extras_require={'test': ['pytest', 'pytest-watch', 'pytest-cov', 'tox']},
    entry_points={
        'console_scripts': [
            "echo_server = run_server:main",
            "echo_client = client:main"
        ]
    }
)
