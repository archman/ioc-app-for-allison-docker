class MySupport1:
    def __init__(self, rec, link):
        pass
    def detach(self, rec):
        pass
    def process(self, rec, reason):
        rec.VAL = rec.VAL + 1

class MySupport2:
    def __init__(self, rec, link):
        pass
    def detach(self, rec):
        pass
    def process(self, rec, reason):
        rec.VAL = rec.VAL + 1 if rec.VAL < 10 else 0

build = MySupport2
