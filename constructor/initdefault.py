class CRectangle(object):
    width = 0.0
    height = 0.0
    
    def __init__(self,iWidth=3.0,iHeight=5.0):
        self.width = iWidth
        self.height = iHeight
        
    def getWidth(self):
        return self.width
    def getHeight(self):
        return self.height

rect1 = CRectangle(2.0)
print(rect1.getWidth())
print(rect1.getHeight())