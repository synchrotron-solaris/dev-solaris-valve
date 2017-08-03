"""
This module can be used to launch a Tango Device Server with two Device
Classes:

* `Valve`
* `FastValve`
"""

# Imports
from valve import Valve
from fast_valve import FastValve
from tango.server import run


def main(args=None, **kwargs):
        return run({"Valve": Valve, "FastValve": FastValve}, args=args, **kwargs)

if __name__ == "__main__":
    main()
