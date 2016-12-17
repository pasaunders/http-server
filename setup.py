"""Setup file for echo server assignment."""


from setuptools import setup


setup(
    name="step1",
    description="A simple HTTP server.",
    version=0.1,
    author="Patrick Saunders and Rick Valenzuela",
    author_email="patrick.a.n.saunders@gmail.com",
    license="MIT",
    py_modules=['http_concurrent', 'client'],
    package_dir={'': 'src'},
    install_requires=['gevent'],
    extras_require={'test': ['pytest', 'pytest-watch', 'pytest-cov', 'tox']},
    entry_points={
        'console_scripts': [
            "echo_server = server:main",
            "echo_client = client:main"
        ]
    }
)
