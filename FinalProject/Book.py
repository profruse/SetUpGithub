class Book:
    def __init__(self, name):
        self.name = str(name)
        self.volumes = 0
        self.popularity = 0

    def addVolume(self):
        self.volumes += 1

    def changePopularity(self, new):
        self.popularity += new
