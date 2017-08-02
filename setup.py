from setuptools import find_packages, setup

from valve.version import __version__, licence
from valve import __doc__, __author__, __author_email__

setup(
    name="tangods-valve",
    author=__author__,
    author_email=__author_email__,
    version=__version__,
    license=licence,
    description="Tango Device Server for valve devices, based on facadedevice "
                "library",
    long_description=__doc__,
    url="https://github.com/synchrotron-solaris/dev-solaris-valve.git",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["setuptools"],
    entry_points={
        "console_scripts": ["Valve = "
                            "valve.valve_ds.valve.Valve:run",
                            "FastValve = "
                            "valve.fast_valve_ds.fast_valve.FastValve:run"]}
)
