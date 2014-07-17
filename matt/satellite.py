from twisted.internet.protocol import Factory, Protocol
from twisted.internet import reactor

class ReceiveChunk(Protocol):
    def dataReceived(self, data):
        print("Broadcasting: " + data)

class ReceiveChunkFactory(Factory):
    def buildProtocol(self, addr):
        return ReceiveChunk()

reactor.listenTCP(1338, ReceiveChunkFactory())
reactor.run()
