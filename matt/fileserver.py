from twisted.internet.protocol import Protocol, Factory, ClientFactory
from twisted.internet import reactor, defer, task
import time, data

BYTES_READ = 1000

class ReceiveRequest(Protocol):
    def __init__(self, factory):
        self.factory = factory

    def dataReceived(self,data):
        data = data.strip("\r\n")
        if data.startswith("vote"):
            self.factory.datastore.vote(data.split("|")[1])
        elif data.startswith("add"):
            args =  data.split("|")
            self.factory.datastore.add(args[1],args[2],args[3])
class ReceiveFactory(Factory):
    def __init__(self, datastore):
        self.datastore = datastore
        
    def buildProtocol(self, addr):
        return ReceiveRequest(self)

class Broadcast(Protocol):
    def __init__(self,factory):
        self.factory = factory

    def connectionMade(self):
        self.try_send()

    def try_send(self):
        sending = self.factory.datastore.get_currently_sending()
        if(sending == "none in schedule"):
            print("Waiting.")
            reactor.callLater(1, self.try_send)
        else:
            self.send_file(sending)

    def send_file(self,sending):
        self.transport.write("begin|{0}|{1}".format(sending.name, sending.size))
        to_broadcast = "x"*(BYTES_READ+1)
        file_to_broadcast = open(sending.path,'r')
        while(len(to_broadcast)>=BYTES_READ):
            to_broadcast=(file_to_broadcast.read(BYTES_READ))
            self.transport.write(to_broadcast)
            
        file_to_broadcast.close()
        self.factory.datastore.next()
        print("Finished broadcast.")

class BroadcastFactory(ClientFactory):
    def __init__(self, datastore):
        self.datastore=datastore

    def buildProtocol(self, addr):
        return Broadcast(self)

def main():
    datastore = data.DownloadData()
    recv_factory = ReceiveFactory(datastore)
    send_factory = BroadcastFactory(datastore)
    reactor.listenTCP(1337, recv_factory)
    reactor.connectTCP('localhost', 1338, send_factory)
    reactor.run()
    
if __name__ == "__main__":
    main()
