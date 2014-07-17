from twisted.protocol import Factory, Protocol

class ReceiveChunk(protocol.Protocol):
    def dataReceived(self, data):
        print("Broadcasting: " + data)
