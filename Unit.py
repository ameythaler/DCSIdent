class Unit:
    def __init__(self, name, nationality, classification):
        self.name = name
        self.nationality = nationality
        self.classification = classification
        self.threats = []
        self.images = []

    def AddThreat(self, threat, threatRange):
        self.threats[threat] = threatRange

    def AddImage(self, image):
        self.images.append(image)

    def ClearImages(self):
        self.images = []

    def RemoveImage(self, image):
        self.images.remove(image)