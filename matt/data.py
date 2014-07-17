
class Download(Object):
    def __init__(self, name, size, votes, times=[]):
        self.name=name
        self.size=size
        self.votes=votes
        self.times=times

class DownloadData(Object):
    def __init__():
        self.downloads=[]
    def vote(name):
        for download in downloads:
            if download.name == name:
                download.votes+=1
                return
    def add(name, size):
        self.downloads.insert(0, Download(name, size, 1, times))
    
    def get_currently_sending():
        return(downloads[0])
