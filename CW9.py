class Homo:
    a = 7
    def __init__(self):
        self.a = 13
    @property
    def oop(self):
        return self.a + 16
    @classmethod
    def cop(cls):
        print(cls.a)



sap = Homo()

print(sap.oop)
sap.cop()
print(sap.a)
