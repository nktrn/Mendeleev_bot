class Element:
    def __init__(self, name='', fullname='', index=0, color=(0, 0, 0)):
        self.name = name
        self.fullname = fullname
        self.index = index
        self.color = color

    def __str__(self):
        return self.name
