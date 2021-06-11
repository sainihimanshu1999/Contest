class Calendar:

    def __init__(self):
        self.stack = []

    def book(self,start,end):
        for s,e in self.stack:
            if start<e and end>s:
                return False
        self.stack.append((start,end))
        return True