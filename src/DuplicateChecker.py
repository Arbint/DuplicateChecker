
class DuplicateChecker():
    def __init__(self):
        self.entries = []

    def SetEntries(self, entriesStr: str):
        self.entries = []
        entriesStr = entriesStr.replace("\n","")
        sperator = "http"
        for url in entriesStr.split(sperator):
            if url == "":
                continue
            url = url.replace(",","")
            url = sperator + url
            self.entries.append(url)             
        
    def GetEntries(self):
        return self.entries

    def FindDuplicates(self):
        seen = set()
        dupRecord = {} # key = email, val = count
        for entry in self.entries:
            if entry not in seen:
                seen.add(entry)
                continue

            if entry in dupRecord:
                dupRecord[entry] += 1
            else:
                dupRecord[entry] = 2
                
        return dupRecord

