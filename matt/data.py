from twisted.internet.protocol import Protocol, Factory, ClientFactory
from twisted.internet import reactor, defer, task
import time

BYTES_READ = 1000

class Download(object):
    def __init__(self, name, size, votes, path):
        self.name=name
        self.size=size
        self.votes=votes
        self.path=path

class DownloadData(object):
    def __init__(self):
        self.downloads=[]

    def vote(self, name):
        for download in self.downloads:
            if download.name == name:
                download.votes+=1
                
                print("Successfully voted for {0}. Total is {1}".format(name, download.votes))
                return
        print("ERROR: Vote for video not found")

    def add(self, name, size, path):
        self.downloads.append(Download(name, size, 1, path))
        print("Added: " + name + " (" + size + "B) to download queue")

    def next(self):
        self.downloads[0].votes = 0
        self.downloads.append(self.downloads[0])
        self.downloads.reverse()
        self.downloads.pop()
        self.downloads.reverse()

    def remove(self, name):
        for download_num in range(len(self.downloads)):
            if self.downloads[download_num].name == name:
                self.downloads.remove(downloads[download_num])
                return

    def get_currently_sending(self):
        try:
            return(self.downloads[0])
        except:
            return("none in schedule")
    def sort_by_votes(self):        
        sort(self.downloads, key= lambda x: x.votes) 
    

class ReceiveRequest(Protocol):
    def __init__(self, factory):
        self.factory = factory

    def dataReceived(self,data):
        data = data.strip("\r\n")
        if data.startswith("vote"):
            self.factory.queue.vote(data.split("|")[1])
        elif data.startswith("add"):
            args =  data.split("|")
            self.factory.queue.add(args[1],args[2],args[3])
class ReceiveFactory(Factory):
    def __init__(self, datastore):
        self.queue = datastore
        
    def buildProtocol(self, addr):
        return ReceiveRequest(self)

class Broadcast(Protocol):
    def __init__(self,factory):
        self.factory = factory

    def connectionMade(self):
        sending = self.factory.datastore.get_currently_sending()
        if(sending == "none in schedule"):
            print("I'm gonna wait.")
            sending = task.deferLater(reactor, 4, self.factory.datastore.get_currently_sending)
            reactor.callLater(1, d.callback, None)
            print("I should have waited.")
        else:
            send_file(sending.path)

    def send_file(self,sending):
        self.transport.write("begin|{0}|{1}".format(sending.name, sending.size))
        to_broadcast = "x"*(BYTES_READ+1)
        file_to_broadcast = open(sending.path,'r')
        while(len(to_broadcast>=BYTES_READ)):
            to_broadcast=(file_to_broadcast.read(BYTES_READ))
            self.transport.write(to_broadcast)
        self.factory.datastore.next()

class BroadcastFactory(ClientFactory):
    def __init__(self, datastore):
        self.datastore=datastore

    def buildProtocol(self, addr):
        return Broadcast(self)

def main():
    datastore = DownloadData()
    recv_factory = ReceiveFactory(datastore)
    send_factory = BroadcastFactory(datastore)
    reactor.listenTCP(1337, recv_factory)
    reactor.connectTCP('localhost', 1338, send_factory)
    reactor.run()
    
if __name__ == "__main__":
    main()
