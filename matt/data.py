from twisted.internet.protocol import Protocol, Factory
from twisted.internet import reactor
import time

class Download(Object):
    def __init__(self, name, size, votes, path, length =0):
        self.name=name
        self.size=size
        self.votes=votes
        self.length=length

class DownloadData(Object):
    def __init__():
        self.downloads=[]

    def vote(name):
        for download in downloads:
            if download.name == name:
                download.votes+=1
                return

    def add(name, size):
        self.downloads.append(Download(name, size, 1, times))
    
    def get_currently_sending():
        return(downloads[0])
    
    def sort_by_votes():        
        sort(self.downloads, key= lambda x: x.votes) 
    

class ReceiveRequest(Protocol):
    def dataReceived(self,data):
        if data.beginswith("vote"):
            self.factory.queue.vote(split(data,"|")[1])
        elif data.beginswith("add"):
            self.factory.queue.add(split(data,"|")[1],split(data,"|")[2])

    def connectionMade(self):
        
class ReceiveFactory(Factory):
    def __init__(self, datastore):
        self.queue = datastore

class Broadcast(Protocol):
    def connectionMade(self):
        sending = datastore.get_currently_sending()
        self.transport.write("begin|{0}|{1}|{2}".format()

class BroadcastFactory(Factory):
    def __init__(self, datastore):
        self.queue = datastore


def main():
    datastore = DownloadData()
    recv_factory = ReceiveFactory(datastore)
    send_factory = BroadcastFactory(datastore)
    reactor.listenTCP(1337, recv_factory)
    reactor.connectTCP('localhost', 1338, send_factory)
    reactor.run()
