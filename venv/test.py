class Animal():
 def __init__(self, name):
  self.name = name
 def who(self):
  return self.name

a = Animal(10)
s= {0:a}
print(s)