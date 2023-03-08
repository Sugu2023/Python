>>> #8.03.2023
>>> empty=
SyntaxError: invalid syntax
>>> empty=()
>>> singleton='hello',
>>> len(empty)
0
>>> len(singleton)
1
>>> singleton
('hello',)
>>> #Sets is an unordered collection with no duplicate elements.
>>> #Curly braces are set() is used to create sets.
>>> #to create empty set u need to use () not {}
>>> players={'virat','rohit','dhoni','rohit','klragul','raina','klragul'}
>>> players
{'raina', 'dhoni', 'klragul', 'rohit', 'virat'}
>>> players
{'raina', 'dhoni', 'klragul', 'rohit', 'virat'}
>>> a=set('Sugumaran')
>>> b=set('Suvedha')
>>> #unique letters in a and b
>>> a-b
{'m', 'n', 'g', 'r'}
>>> a&b
{'u', 'a', 'S'}
>>> a|b
{'u', 'g', 'r', 'a', 'S', 'm', 'd', 'n', 'v', 'h', 'e'}
>>> a^b
{'g', 'm', 'd', 'n', 'v', 'h', 'r', 'e'}
>>> #Dictionaries
>>> thisdict={'name':'Suvedha','age':21,'role':'ABPM'}
>>> print(thisdict)
{'name': 'Suvedha', 'age': 21, 'role': 'ABPM'}
>>> thisdict[name]
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#23>", line 1, in <module>
NameError: name 'name' is not defined
>>> thisdict['name']
'Suvedha'
>>> thisdict['role']='ASP OFFICER'
>>> thisdict
{'name': 'Suvedha', 'age': 21, 'role': 'ASP OFFICER'}
>>> #above is an example that we can change the value of the dictionary.
>>> #using len function we can know the length of the dictionary
>>> len(thisdict)
3
>>> type(dict)
<class 'type'>
>>> type(set)
<class 'type'>
>>> type(list)
<class 'type'>
>>> type(tuple)
<class 'type'>
>>> #we can create dictionary using dict() constructor also
>>> thisdict1=dict('brand':'Bajaj','model':2004,'name':'boxer')
SyntaxError: invalid syntax
>>> #In constructor we need to need to use = symbol instead of :
>>> thisdict1=dict('brand'='Bajaj','model'=2004,'name'='boxer')
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
>>> #and we dont want to make that ''
>>> thisdict1=dict(brand:'Bajaj',model:2004,name='boxer')
SyntaxError: invalid syntax
>>> thisdict1=dict(brand='Bajaj',model=2004,name='boxer')
>>> thisdict1
{'brand': 'Bajaj', 'model': 2004, 'name': 'boxer'}
>>> 
