class Book:
    def __init__(self, name):
        self.name = str(name)
        self.volumes = 0
        self.popularity = 0
        self.complete = False

    def addVolume(self):  # Methods to change important values
        self.volumes += 1

    def changePopularity(self, new):
        self.popularity += new

    def completed(self):
        self.complete = True
