"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

from io import open
from setuptools import find_packages
from setuptools import setup
from setuptools.command.install import install

import os
import sys

here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

with open(os.path.join(here, "CHANGELOG.md"), encoding="utf-8") as f:
    long_description += "\n\n" + f.read()


VERSION = "0.4.0"


class VerifyVersionCommand(install):
    """Custom command to verify that the git tag matches our version.

    Taken from https://circleci.com/blog/continuously-deploying-python-packages-to-pypi-with-circleci/
    """

    description = "verify that the git tag matches our version"

    def run(self):  # noqa: D102
        tag = os.getenv("CIRCLE_TAG")

        if tag != VERSION:
            info = "Git tag: {0} does not match the version of this app: {1}".format(
                tag, VERSION
            )
            sys.exit(info)

testing_extras = [
    "pytest >= 3.1.0",  # >= 3.1.0 so we can use pytest.param
    "coverage",
    "pytest-cov",
    "pytest-xdist",
]

setup(
    name="pyramid_openapi3",
    version=VERSION,
    description="Pyramid addon for OpenAPI3 validation",
    long_description=long_description,
    license="MIT",
    long_description_content_type="text/markdown",
    url="https://github.com/Pylons/pyramid_openapi3",
    author="niteo.co",
    author_email="info@niteo.co",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    keywords="pyramid openapi3 openapi rest restful",
    packages=find_packages(exclude=["tests"]),
    package_data={"pyramid_openapi3": ["static/*.*"], "": ["LICENSE"]},
    install_requires=["openapi-core", "openapi-spec-validator", "pyramid"],
    extras_require={"testing": testing_extras, ':python_version<"3.7"': ["importlib-resources"]},
    cmdclass={"verify": VerifyVersionCommand},
)
