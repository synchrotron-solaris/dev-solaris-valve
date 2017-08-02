"""
This module contains device class Valve and run method for it.
"""

# Imports
from tango import DevState, AttrWriteType, DispLevel
from facadedevice import Facade, proxy_attribute, proxy_command, state_attribute


class Valve(Facade):
    """
    This class implements Tango device server for control of basic vacuum valves.
    Each Tango device represents one vacuum valve, which can be in open or closed.

    The Tango device works on a set of four PLC attributes of type DevShort,
    which must be exposed by PLC device server.

    OpenS PLC attribute should be True when valve is open and False when it is closed
    ClosedS PLC attribute should be True when valve is closed and False when it is opened

    OpenC PLC attribute should cause valve to open if it is closed
    CloseC PLC attribute should cause valve to close if it is open
    """

    def safe_init_device(self):
        """
        This is a method to safely initialize the Valve device,
        overrode from Facade base class
        """
        super(Valve, self).safe_init_device()
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
        access=AttrWriteType.READ_WRITE,
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

    # state attributes

    @state_attribute(
        bind=['ValveInterlock', 'ValveCutOff', 'ValveOpen', 'ValveClosed',
              'UnexpectedState'])
    def state_and_status(self, interlock, cutoff, opn, closed, unexp):
        """
        This method changes state of device, accordingly to device attributes.
        :param interlock: ValveInterlock
        :param cutoff: ValveCutOff
        :param opn: ValveOpen
        :param closed: ValveClosed
        :param unexp: UnexpectedState
        :return: appropriate device state and status
        :rtype: DevState
        """
        if interlock:
            return DevState.ALARM, "Valve is interlocked"
        elif cutoff:
            return DevState.CLOSE, "Valve has been cut off. It's closed now and " \
                                   "remote control is not possible"
        elif closed:
            return DevState.CLOSE, "Valve is closed"
        elif opn:
            return DevState.OPEN, "Valve is open"
        elif unexp:
            return DevState.UNKNOWN, "Unexpected state"
        return DevState.ON, "Device is running"

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
    Valve.run_server()
