from twisted.protocol import Protocol, Factory
import time

class Download(Object):
    def __init__(self, name, size, votes, length =0):
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
    

class ReceiveRequest(protocol.Protocol):
    def dataReceived(self,data):
        if data.beginswith("vote"):
            self.factory.queue.vote(split(data,"|")[1])
        elif data.beginswith("add"):
            self.factory.queue.add(split(data,"|")[1],split(data,"|")[2])
    def connectionMade(self):
        
class ReceiveFactory(protocol.Factory):
    def __init__(datastore):
        self.queue = datastore

class BroadCast(protocol.Protocol):
    

def main():
    datastore = DownloadData()
    factory = ReceiveFactory(datastore)
    reactor.listenTCP(factory, 1337)
