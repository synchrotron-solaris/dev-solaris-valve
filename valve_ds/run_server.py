"""
Module to run device server
"""

# Imports
from valve import Valve
from fast_valve import FastValve
from tango.server import run


# run server

if __name__ == "__main__":
    run({"Valve": Valve, "FastValve": FastValve})