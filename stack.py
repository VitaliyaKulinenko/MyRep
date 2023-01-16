class OurStack:

    def __init__(self):
        self.stack = []
        self.max_value= None
        self.max_collection=[]
    def pop(self):
        value=self.stack.pop()
        if self.max_value == value:
            del self.max_collection[-1]


        return value




    def push(self,value):
        if self.max_value is None:
            self.max_value=value
        if self.max_value < value:
            self.max_value = value
            self.max_collection.append(self.max_value)

        self.stack.append(value)
    def max(self):
        return self.max_collection[-1]
    def __str__(self):
        return ''.join(str(self.stack))


s = OurStack()
s.push(3)
s.push(5)
s.pop()
s.push(10)
s.push(15)
s.push(12)
s.push(56)


print(s)
print(s.max_value)
