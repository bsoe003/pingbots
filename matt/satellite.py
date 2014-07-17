from twisted.protocol import Factory, Protocol

class ReceiveChunk(protocol.Protocol):
    def dataReceived(self, data):
        print("Broadcasting: " + data)

class ReceiveChunkFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return ReceiveChunk()

reactor.listenTCP(1338, ReceiveChunkFactory())
