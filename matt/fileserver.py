from twisted.protocol import Protocol, Factory

#message format: "vote|name", "add|name|size"

class ReceiveRequest(protocol.Protocol):
    def dataReceived(self,data):
        if data.beginswith("vote"):
            self.factory.queue.vote(split(data,"|")[1])
        elif data.beginswith("add"):
            self.factory.queue.add(split(data,"|")[1],split(data,"|")[2])
    def connectionMade(self):
        
class ReceiveFactory(protocol.Factory):
    def __init__():
        self.queue = DownloadData()


class SendRequest(protocol.Protocol):
    pass

factory = ReceiveFactory()
reactor.listenTCP(factory, 1337)
