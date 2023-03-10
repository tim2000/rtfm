import mido
import pytemidi
import time


def get_new_device(name):
    print(pytemidi.get_driver_version())
    print(pytemidi.get_library_version())

    dev = pytemidi.Device("RTFM")
    dev.create()

    return dev


class MidoDevice:
    def __init__(self) -> None:
        self.device = get_new_device("RTFM")
    
    def send_note_on_off(self, channel, note):
        self.device.send(mido.Message("note_on", channel=channel, note=note, velocity=127).bin())
        time.sleep(0.2)
        self.device.send(mido.Message("note_off", channel=channel, note=note, velocity=127).bin())

    def send_cc(self, channel, cc):
        # CC only support trigger atm
        self.device.send(mido.Message("control_change", channel=channel, control=cc, value=0).bin())
        time.sleep(0.2)
        self.device.send(mido.Message("control_change", channel=channel, control=cc, value=127).bin())
