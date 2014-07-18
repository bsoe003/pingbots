from twisted.internet.protocol import Factory, Protocol
from twisted.internet import reactor
import sys

class ReceiveChunk(Protocol):
    def __init__(self):
        self.reading = False
        self.curr_path = ""
        self.file_desc = None

    def dataReceived(self, data):
        if(self.reading):
            if(data.strip("\r\n")=="end transmission"):
                self.file_desc.close()
                return
            self.file_desc.write(data)
        elif(data.startswith("begin")):
            self.curr_path = data[5::].strip("\r\n")
            out = open(self.curr_path, 'w')
            self.reading = True

                          
class ReceiveChunkFactory(Factory):
    def buildProtocol(self, addr):
        return ReceiveChunk()

reactor.listenTCP(1338, ReceiveChunkFactory())
reactor.run()
