#constror is  function automatically called object is created 
class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s = student("mani reethika", 22)

print(s.name)
print(s.age)
