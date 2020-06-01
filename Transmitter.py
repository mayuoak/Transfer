class Transmitter(object):
    def __init__(self, file_name):
        self.file_name = file_name
        self.transmit()

    def _read_extension(self):
        pass

    def _read_size(self):
        pass

    def transmit(self):
        ## IDEA: get extension
        ## IDEA: get size
        ## IDEA: start server, show IP and wait for connection
        ## IDEA: if connection established, do following things
        ## IDEA: 1. transmit and acknowledge size
        ## IDEA: 2. transmit and acknowledge extension
        ## IDEA: 3. transmit and acknowledge individual packets in bytes
        ## IDEA: once transmitted close transmitter after closing port
