from twisted.protocol import Protocol, Factory

class ReceiveRequest(protocol.Protocol):
    def dataReceived(self,data):
        self.factory.queue.vote(data)
    def connectionMade(self):
        
class ReceiveFactory(protocol.Factory):
    def __init__():
        self.data = DownloadData()


class SendRequest(protocol.Protocol):
    pass
