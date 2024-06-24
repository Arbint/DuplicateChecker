
class DuplicateChecker():
    def __init__(self):
        self.entries=[]

    def SetEntries(self, entriesStr: str, sperator: str):
        entriesStr = entriesStr.replace("\n","")
        self.entries = entriesStr.split(sperator)
        self.entries = [element for element in self.entries if element != ""]

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

