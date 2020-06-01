class Receiver(object):
    def __init__(self, ip):
        if ip == None:
            #ask transmitter ip
        else:
            self.ip = ip

    def receive(self):
        ## IDEA: with given ip try to eshtablish connection with transmitter
        ## IDEA: receive size
        ## IDEA: receive extension
        ## IDEA: start receiving packets and sending acknowledgement
        ## IDEA: once received all packets save file and close connection
