import os


class packet(object):
    def __init__(self, id, packet_type=None, data=None):
        self.packet_type = packet_type
        self.id = id
        self.data = data
        self.ack = False
        self._make_packet()

    def _make_packet(self):
        ## IDEA: logic to build a packet
        pass

class Transmitter(object):
    def __init__(self, file_name):
        self.file_name = file_name
        self.extension = ""
        self.size = ""
        self.transmit()

    def _get_extension(self):
        file_name, file_extension = os.path.splitext(self.file_name)
        return file_extension

    def _get_size(self):
        return os.stat(self.file_name).st_size

    def _start_server(self):
        print("server started")
        return True

    def _transmit_size(self):
        print("size transmitted")
        return True

    def _transmit_extension(self):
        print("extension transmitted")
        return True

    def _transmit_packet(self, packet):
        print("packet transmitted: {0}".format(packet.id))
        return True

    def _tranmit_packets(self):
        return self._transmit_packet(packet(1))

    def _wait_for_packet_acknowledgement(self, packet):
        pass

    def transmit(self):
        self.extension = self._get_extension()
        self.size = self._get_size()
        self._start_server()
        self._transmit_size()
        self._transmit_extension()
        self._tranmit_packets()

t = Transmitter("README.md")
