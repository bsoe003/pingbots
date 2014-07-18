from twisted.internet.protocol import Protocol, Factory, ClientFactory
from twisted.internet import reactor, defer, task
import time, os

BYTES_READ = 1000

class Download(object):
    def __init__(self, name, votes, path, size=0):
        self.name=name
        self.size = size
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

    def add(self, name, path, size=0):
        nsize = os.stat(path).st_size
        self.downloads.append(Download(name=name, size=nsize, votes=1, path=path))
        print("Added: " + name + " (" + str(nsize) + "B) to download queue")

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
