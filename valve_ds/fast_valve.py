"""
This module contains device class Valve and run method for it.
"""

# Imports
from tango import DevState, AttrWriteType, DispLevel
from facadedevice import Facade, proxy_attribute, proxy_command


class FastValve(Facade):
    """
    This class implements Tango device server for control of vacuum valves with
    two air-inrush sensors.
    Each Tango device represents one vacuum valve, which can be in open or closed.

    The Tango device works on a set of six PLC attributes of type DevShort, which
    must be exposed by PLC device server.

    OpenS PLC attribute should be True when valve is open and False when it is
    closed.
    ClosedS PLC attribute should be True when valve is closed and False when it
    is opened.

    OpenC PLC attribute should cause valve to open if it is closed.
    CloseC PLC attribute should cause valve to close if it is open.

    InrushA1 should be True if air-inrush is detected on first sensor or False
    in normal state.
    InrushA2 should be True if air-inrush is detected on second sensor or False
    in normal state.
    """

    def safe_init_device(self):
        """
        This is a method to safely initialize the Valve device,
        overrode from Facade base class
        """
        super(FastValve, self).safe_init_device()
        self.set_state(DevState.ON)
        self.set_status("Device is running.")

    # proxy attributes

    ValveOpen = proxy_attribute(
        dtype=bool,
        access=AttrWriteType.READ_WRITE,
        property_name="PLCAttrName_OpenS",
        display_level=DispLevel.OPERATOR,
        description="Attribute that represents PLC signal for valve open "
                    "state.")

    ValveClosed = proxy_attribute(
        dtype=bool,
        access=AttrWriteType.READ_WRITE,
        property_name="PLCAttrName_ClosedS",
        display_level=DispLevel.OPERATOR,
        description="Attribute that represents PLC signal for valve closed "
                    "state.")

    ValveInterlock = proxy_attribute(
        dtype=bool,
        access=AttrWriteType.READ,
        property_name="PLCAttrName_InterlockA",
        display_level=DispLevel.OPERATOR,
        description="Attribute that represents PLC signal for valve in "
                    "interlock alarm.")

    ValveCutOff = proxy_attribute(
        dtype=bool,
        access=AttrWriteType.READ_WRITE,
        property_name="PLCAttrName_CutOffA",
        display_level=DispLevel.OPERATOR,
        description="Attribute that represents PLC signal for valve in cut-off "
                    "state. Valve can only be put to cut-off state via manual "
                    "control on the device. In this state the valve is closed, "
                    "power to the valve was cut off and remote control of the "
                    "valve is not possible.")

    UnexpectedState = proxy_attribute(
        dtype=bool,
        access=AttrWriteType.READ_WRITE,
        property_name="PLCAttrName_UnexpectedState",
        display_level=DispLevel.OPERATOR,
        description="Attribute that represents PLC signal for valve in unexpected "
                    "state.")

    InRush1A = proxy_attribute(
        dtype=bool,
        access=AttrWriteType.READ_WRITE,
        property_name="PLCAttrName_Inrush1A",
        display_level=DispLevel.OPERATOR,
        description="Name of the PLC device attribute that represents PLC signal"
                    " for air inrush alarm on the first valve sensor.")

    InRush2A = proxy_attribute(
        dtype=bool,
        access=AttrWriteType.READ_WRITE,
        property_name="PLCAttrName_Inrush2A",
        display_level=DispLevel.OPERATOR,
        description="Name of the PLC device attribute that represents PLC signal"
                    " for air inrush alarm on the second valve sensor.")

    # proxy commands

    @proxy_command(
        dtype_out=bool,
        write_attribute=True,
        property_name="PLCAttrName_OpenC",
        doc_out="True to PLCAttrName_OpenC")
    def Open(self, subcommand):
        """
         :rtype: bool
        """
        subcommand(True)
        return True

    @proxy_command(
        dtype_out=bool,
        write_attribute=True,
        property_name="PLCAttrName_CloseC",
        doc_out="True to PLCAttrName_CloseC")
    def Close(self, subcommand):
        """
        :rtype: bool
        """
        subcommand(True)
        return True

# run server

if __name__ == '__main__':
    FastValve.run_server()