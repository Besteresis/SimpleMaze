class Cube:
    def __init__(self, border, posX, posY):
        self.border = border
        self.posX = posX
        self.posY = posY

    def setBorder(self, border):
        self.border = border

    def getBorder(self):
        return self.border

    def getPosX(self):
        return self.posX

    def getPosY(self):
        return self.posY