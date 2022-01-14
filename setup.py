from setuptools import find_packages, setup

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="matatika_sendgrid_cli",
    version="0.1.0",
    description="A Python CLI for sending emails with sendgrid.",
    author="DanielPDWalker",
    url="https://www.matatika.com/",
    entry_points="""
        [console_scripts]
        sendgrid=sendgrid_cli.cli.commands.root:sendgrid_cli
    """,
    license="MIT",
    install_requires=required,
    packages=find_packages(exclude=("tests")),
    include_package_data=True,
)
