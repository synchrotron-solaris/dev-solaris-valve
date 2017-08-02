"""
This module contains device class Valve and run method for it.
"""

# Imports
from tango import DevState, AttrWriteType, DispLevel
from facadedevice import proxy_attribute
from valve import Valve


class FastValve(Valve):
    """
    InrushA1 should be True if air-inrush is detected on first sensor or False
    in normal state.
    InrushA2 should be True if air-inrush is detected on second sensor or False
    in normal state.
    """
    __doc__ = Valve.__doc__ + __doc__

    def safe_init_device(self):
        """
        This is a method to safely initialize the Valve device,
        overriding same method from Facade Device Class - Valve
        """
        super(FastValve, self).safe_init_device()
        self.set_state(DevState.ON)
        self.set_status("Device is running.")

    InRush1A = proxy_attribute(
        dtype=bool,
        access=AttrWriteType.READ,
        property_name="PLCAttrName_Inrush1A",
        display_level=DispLevel.OPERATOR,
        description="Name of the PLC device attribute that represents PLC signal"
                    " for air inrush alarm on the first valve sensor.")

    InRush2A = proxy_attribute(
        dtype=bool,
        access=AttrWriteType.READ,
        property_name="PLCAttrName_Inrush2A",
        display_level=DispLevel.OPERATOR,
        description="Name of the PLC device attribute that represents PLC signal"
                    " for air inrush alarm on the second valve sensor.")

# run server

if __name__ == '__main__':
    FastValve.run_server()
