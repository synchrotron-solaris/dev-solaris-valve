"""
VALVE
=====

This whole package contains three Device Classes for valves, based on
facadedevice library.

* Valve
* FastValve

"""

from setuptools import find_packages

__all__ = ['run_server', 'valve', 'fast_valve', 'version']
__doc__ = ""
__author__ = "Stanislaw Cabala"
__author_email__ = "stanislaw.cabala@gmail.com"

for package_name in find_packages():
    package_import = __import__(package_name)
    __doc__ += "%s: %s" % (package_name, package_import.__doc__)
    __author__ += package_import.__author__ + ", "
    __author_email__ += package_import.__author_email__ + ", "
