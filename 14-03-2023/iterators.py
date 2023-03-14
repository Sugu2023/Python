mylist=[1,2,3,'Sugu']
print(mylist)
myiterator=iter(mylist)
print(myiterator)
# print(myiterator.__next__())
# print(myiterator.__next__())

#stop iteration
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)
