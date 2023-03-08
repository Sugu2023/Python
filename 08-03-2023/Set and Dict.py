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
##-------------------------------------------------------------------------
>>> thisdict=['name':'sugu',age:21,'location':'elandhai'}
SyntaxError: invalid syntax
>>> thisdict={'name':'sugu',age:21,'location':'elandhai'}
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#1>", line 1, in <module>
NameError: name 'age' is not defined
>>> thisdict=['name':'sugu','age':21,'location':'elandhai'}
SyntaxError: invalid syntax
>>> thisdict={'name':'sugu','age':21,'location':'elandhai'}
>>> thisdict
{'name': 'sugu', 'age': 21, 'location': 'elandhai'}
>>> #methods
>>> thisdict.get('name')
'sugu'
>>> #using key also we can get cvalue
>>> thisdict['name']
'sugu'
>>> #to know all the keys
>>> thisdict.keys()
dict_keys(['name', 'age', 'location'])
>>> #we can add key
>>> thisdict['gender']='male'
>>> thisdict.keys()
dict_keys(['name', 'age', 'location', 'gender'])
>>> thisdict
{'name': 'sugu', 'age': 21, 'location': 'elandhai', 'gender': 'male'}
>>> #to know all the values
>>> thisdict.values()
dict_values(['sugu', 21, 'elandhai', 'male'])
>>> #each item
>>> thisdict.items()
dict_items([('name', 'sugu'), ('age', 21), ('location', 'elandhai'), ('gender', 'male')])
>>> #we can check whether the key is present in the dictionary
>>> if gender in thisdict:
	print('Yes 'gender' is present in the dictionary')
	
SyntaxError: invalid syntax
>>> if 'gender' in thisdict:
	print("yes 'gender' is present in thisdict")

yes 'gender' is present in thisdict
>>> #we can update the value of the dictionary
>>> thisdict.update({'name':'Thiru'})
>>> thisdict
{'name': 'Thiru', 'age': 21, 'location': 'elandhai', 'gender': 'male'}
>>> #remove items
>>> thisdict.pop('gender')
'male'
>>> thisdict
{'name': 'Thiru', 'age': 21, 'location': 'elandhai'}
>>> thisdict.pop()
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#31>", line 1, in <module>
TypeError: pop expected at least 1 argument, got 0
>>> #del can delete the entire dictionary
>>> thisdict['role']='Student'
>>> thisdict
{'name': 'Thiru', 'age': 21, 'location': 'elandhai', 'role': 'Student'}
>>> thisdict.del('age')
SyntaxError: invalid syntax
>>> del thisdict['age']
>>> thisdict
{'name': 'Thiru', 'location': 'elandhai', 'role': 'Student'}
>>> thisdict.clear()
>>> thisdict
{}
>>> #clear() it empties the dictionary
>>> #copy --it copies the key and value in one dictionary to another dictionary
>>> players=dict(captain='Dhoni',vc='Kohli',batsmen='Rohit',wk='Pant',bowler='Boom',allround='Jaddu')
>>> players.values()
dict_values(['Dhoni', 'Kohli', 'Rohit', 'Pant', 'Boom', 'Jaddu'])
>>> players_details.copy(players)
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#44>", line 1, in <module>
NameError: name 'players_details' is not defined
>>> players_details=players.copy()
>>> players_details
{'captain': 'Dhoni', 'vc': 'Kohli', 'batsmen': 'Rohit', 'wk': 'Pant', 'bowler': 'Boom', 'allround': 'Jaddu'}
>>> players_details['spinner':'ash']
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#47>", line 1, in <module>
TypeError: unhashable type: 'slice'
>>> players_details['spinner']='ash'
>>> players
{'captain': 'Dhoni', 'vc': 'Kohli', 'batsmen': 'Rohit', 'wk': 'Pant', 'bowler': 'Boom', 'allround': 'Jaddu'}
>>> #nested dictionaries
>>> myfamily={
	'child1':{
		'name':'Emi',
		'year':2005
		},
	'child2':
	{
		'name':'mei',
		year:2006
		}
	}
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#61>", line 9, in <module>
NameError: name 'year' is not defined
>>> myfamily={
	'child1':{
		'name':'Emi',
		'year':2005
		},
	'child2':
	{
		'name':'mei',
		'year':2006
		}
	}
>>> myfamily
{'child1': {'name': 'Emi', 'year': 2005}, 'child2': {'name': 'mei', 'year': 2006}}
>>> #ACCESSNG In nestted child
>>> myfamily['child2']['year']
2006

