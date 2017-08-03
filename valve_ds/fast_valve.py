"""
This module contains device class Valve and run method for it.
"""

# Imports
from tango import DevState, AttrWriteType, DispLevel
from facadedevice import proxy_attribute, state_attribute
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

    # proxy attributes

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

    # state attributes

    @state_attribute(
        bind=['ValveInterlock', 'ValveCutOff', 'ValveOpen', 'ValveClosed',
              'UnexpectedState', 'InRush1A', 'InRush2A'])
    def state_and_status_fast_valve(self, interlock, cutoff, opn, closed, unexp, rush1, rush2):
        """
        This method changes state of device, accordingly to device attributes.

        :param interlock: ValveInterlock
        :param cutoff: ValveCutOff
        :param opn: ValveOpen
        :param closed: ValveClosed
        :param unexp: UnexpectedState
        :param rush1: InRush1A
        :param rush2: InRush2A

        :return: appropriate device state and status

        :rtype: DevState
        """

        state, status = self.state_and_status(interlock, cutoff, opn, closed,
                                                unexp)
        if rush1 or rush2:
            return DevState.ALARM, "One or both of the valve sensors is in " \
                                   "alarm state due to air inrush"
        else:
            return state, status

# run server

if __name__ == '__main__':
    FastValve.run_server()
