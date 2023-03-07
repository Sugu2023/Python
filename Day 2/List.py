Python 3.8.10 (default, Nov 14 2022, 12:59:47) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> #List--It is a built in datatype that allow you to store a collection of value.
>>> list=[1,2,3,4,5]
>>> list
[1, 2, 3, 4, 5]
>>> list[4]
5
>>> list[-3]
3
>>> list[-2:]
[4, 5]
>>> list[:-2]
[1, 2, 3]
>>> list+[6,7,8,9,10]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> lsit
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#8>", line 1, in <module>
NameError: name 'lsit' is not defined
>>> list
[1, 2, 3, 4, 5]
>>> #WHILE String is immutable so we cannot change the value in it. But in list we can change the value.
>>> list[4]=24
>>> list
[1, 2, 3, 4, 24]
>>> mylist=['applle',3,'orane',true]
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#13>", line 1, in <module>
NameError: name 'true' is not defined
>>> mylist=['apple',1,'orange',True]
>>> mylist
['apple', 1, 'orange', True]
>>> mylist[-1]
True
>>> list*3
[1, 2, 3, 4, 24, 1, 2, 3, 4, 24, 1, 2, 3, 4, 24]
>>> (list)*4
[1, 2, 3, 4, 24, 1, 2, 3, 4, 24, 1, 2, 3, 4, 24, 1, 2, 3, 4, 24]
>>> mylist.append(False)
>>> mylist
['apple', 1, 'orange', True, False]
>>> mylist[2:4]=['jack',1]
>>> mylist
['apple', 1, 'jack', 1, False]
>>> mylist
['apple', 1, 'jack', 1, False]
>>> mylist[3:5]=[2,4,5]
>>> mylist
['apple', 1, 'jack', 2, 4, 5]
>>> letters=['a','b','c','d','e','f']
>>> letters[0:2]=['A','B','C']
>>> letters
['A', 'B', 'C', 'c', 'd', 'e', 'f']
>>> letterlist=[1,2,3,4,5,6,7]
>>> letterlist[1:2]=[10,20,30]
>>> letterlist
[1, 10, 20, 30, 3, 4, 5, 6, 7]
>>> letterlist[1:2]=[10,20,30.40,50]
>>> letterlist
[1, 10, 20, 30.4, 50, 20, 30, 3, 4, 5, 6, 7]
>>> len(letterlist)
12
>>> #nest list
>>> a=['a','b','c']
>>> n=[1,2,3]
>>> x=[a,n]
>>> x
[['a', 'b', 'c'], [1, 2, 3]]
>>> x[0]
['a', 'b', 'c']
>>> x[1]
[1, 2, 3]
>>> #methods in List
>>> mylist=[1,2,3,4,5]
>>> mylist.append(6,7)
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#44>", line 1, in <module>
TypeError: append() takes exactly one argument (2 given)
>>> #one thing we must need to knoe append only add one argument at a time.
>>> #for this only there came a method extend.
>>> mylist1=[6,7,8,9,10]
>>> mylist.append(mylist1)
>>> mylist
[1, 2, 3, 4, 5, [6, 7, 8, 9, 10]]
>>> #if we append another list in the list it may join but it will separate.
>>> mylist.extend(mylist1)
>>> mylist
[1, 2, 3, 4, 5, [6, 7, 8, 9, 10], 6, 7, 8, 9, 10]
>>> #Better i try with another example
>>> List1=['a','b','c','d']
>>> List2=[1,2,3,4]
>>> List1.extend(List2)
>>> List1
['a', 'b', 'c', 'd', 1, 2, 3, 4]
>>> #-------------------------------------------
>>> #Insert
>>> List1.insert('a',0)
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#60>", line 1, in <module>
TypeError: 'str' object cannot be interpreted as an integer
>>> List1.insert(0,x)
>>> List1
[[['a', 'b', 'c'], [1, 2, 3]], 'a', 'b', 'c', 'd', 1, 2, 3, 4]
>>> List3=[10,20,30,40,60]
>>> List3.insert(4,50)
>>> List3
[10, 20, 30, 40, 50, 60]
>>> #--------------------------------------------------------------
>>> List3.remove(40)
>>> List3
[10, 20, 30, 50, 60]
>>> List3.insert(3,40)
>>> List3.remove(70)#if element is not present it scold us by giving type error.
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#70>", line 1, in <module>
ValueError: list.remove(x): x not in list
>>> #--------------------------------------------------------------------
>>> #pop
>>> 
List1=[1,2,3,4,5]
print(List1)
List2=['a','b','c','d']
List1.append(List2)
print(List1)
List1.extend(List2)
print(List1)
List3=[1,2,4,5,6]
List3.insert(3,2)
print(List3)
List3.remove(4)
print(List3)
List3.insert(3,2)
List3.insert(4,3)
print(List3)
List4=['a','c','e']
List4.insert(1,'b')
List4.insert(3,'d')
print(List4)
List4.pop(3)
print(List4)
List5=['a','b','c','d','s','t','s','u']
x=List5.count('s')
print(x)
List6=[10,9,8,7,6,5,4,3,2,1]
List6.reverse()
print(List6)
List7=[99,77,5,344,0,32,2,56]
List7.sort()
print(List7)
List8=['Sugu','Suve','Thiru','Kokila','Ram']
List9=List8.copy()
print(List9)
List9.pop()
del List9[2]
print(List9)



#List Comprehensions
squares=[]
for i in range(10):
    squares.append(i*2)
print(squares)
