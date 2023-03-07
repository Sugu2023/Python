Python 3.8.10 (default, Nov 14 2022, 12:59:47) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> mytuple1=(1,2,3,4,'foo',9.0)
>>> print(mytuple)
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#1>", line 1, in <module>
NameError: name 'mytuple' is not defined
>>> print(mytuple1)
(1, 2, 3, 4, 'foo', 9.0)
>>> mytuple2=(10,20,30,40)
>>> mytuple3=(mytuple1,mytuple2)
>>> mytuple3
((1, 2, 3, 4, 'foo', 9.0), (10, 20, 30, 40))
>>> #Tuple are cannot be modified once set.
>>> mytuple1[0]='Sugu'
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#7>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> #but we can create mutable objects like list inside Tuple.
>>> mytuple4=([1,2,3],[10,20,30])
>>> mytuple4[0]
[1, 2, 3]
>>> mytuple4[0][1]
2
>>> mytuple[0][3]='Sugu'
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#12>", line 1, in <module>
NameError: name 'mytuple' is not defined
>>> mytuple4[0][3]='Sugu'
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#13>", line 1, in <module>
IndexError: list assignment index out of range
>>> mytuple[0][2]='Sugu'
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#14>", line 1, in <module>
NameError: name 'mytuple' is not defined
>>> mytuple4[0][3]='Sugu'
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#15>", line 1, in <module>
IndexError: list assignment index out of range
>>> mytuple4[0][2]='Sugu'
>>> mytuple4
([1, 2, 'Sugu'], [10, 20, 30])
>>> #we can modify mutable objects inside tuple.
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> 
