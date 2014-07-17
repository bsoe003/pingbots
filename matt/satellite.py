from twisted.internet.protocol import Factory, Protocol
from twisted.internet import reactor
import sys

class ReceiveChunk(Protocol):
    def dataReceived(self, data):
        sys.stdout.write("Broadcasting: " + data)

class ReceiveChunkFactory(Factory):
    def buildProtocol(self, addr):
        return ReceiveChunk()

reactor.listenTCP(1338, ReceiveChunkFactory())
reactor.run()
