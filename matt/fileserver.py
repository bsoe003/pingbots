from twisted.protocol import Protocol, Factory

#message format: "vote|name", "add<name>|size"

class ReceiveRequest(protocol.Protocol):
    def dataReceived(self,data):
        if data.beginswith("vote"):
            self.factory.queue.vote(data)
        elif data.beginswith("add"):
            
    def connectionMade(self):
        
class ReceiveFactory(protocol.Factory):
    def __init__():
        self.queue = DownloadData()


class SendRequest(protocol.Protocol):
    pass
