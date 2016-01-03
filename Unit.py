class Unit:
    def __init__(self, name, nationality, classification):
        self.name = name
        self.nationality = nationality
        self.classification = classification
        self.threats = []  # array of [threat type, threat range]
        self.images = []

    def AddThreat(self, threat):
        self.threats.append(threat)

    def ClearThreats(self):
        self.threats = []

    def RemoveThreat(self, threat):
        remIdx = -1
        idx = 0
        for curThreat in self.threats:
            if curThreat[0] == threat:
                remIdx = idx
                break
            idx += 1
        if remIdx != -1:
            self.threats.remove(remIdx)

    def AddImage(self, image):
        self.images.append(image)

    def ClearImages(self):
        self.images = []

    def RemoveImage(self, image):
        self.images.remove(image)