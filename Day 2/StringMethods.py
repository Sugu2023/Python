Python 3.8.10 (default, Nov 14 2022, 12:59:47) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> #String methods
>>> S='sugu'
>>> S.capitalize()
'Sugu'
>>> #capitalize method will change the first letter only capital and rest lowercase.
>>> S.casefold()
'sugu'
>>> name='sathur'
>>> name
'sathur'
>>> 'sathur'
'sathur'
>>> var=10
>>> var
10
>>> var+10
20
>>> 'sugu'+'sathur'
'sugusathur'
>>> stri='SUGUMARAN%^'
>>> stri.casefold()
'sugumaran%^'
>>> stringcenet='Kokila'
>>> stringcenter.center(40,'.')
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#15>", line 1, in <module>
NameError: name 'stringcenter' is not defined
>>> stringcenet=center(50,'*')
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#16>", line 1, in <module>
NameError: name 'center' is not defined
>>> stringcenet.center(50,'*')
'**********************Kokila**********************'
>>> strcount='Sugumaran'
>>> strcount.count('u',[0[,9]])
SyntaxError: invalid syntax
>>> strcount.count('u'[,0[,9]])
SyntaxError: invalid syntax
>>> strcount.count('u')
2
>>> strcount.count('u',0,4)
2
>>> strcount.count('u',0,2)
1
>>> strcount.endswith('ran')
True
>>> strcount.find('ma')
4
>>> strcount.find('an')
7
>>> strcount.index('m')
4
>>> strexp='Hi\thello\thow are you>'
>>> strexp.expandtabs(4)
'Hi  hello   how are you>'
>>> strexp
'Hi\thello\thow are you>'
>>> friend1='Sugu'
>>> friend2='Thiru'
>>> str3='{}and{} are brothers.'format(friend1,friend2)
SyntaxError: invalid syntax
>>> str3="{}and{} are brothers.".format(friend1,friend2)
>>> print(str3)
SuguandThiru are brothers.
>>> str3="{}and{} are brothers.".format(friend1,friend2)
>>> str3="{} and {} are brothers.".format(friend1,friend2)
>>> str3
'Sugu and Thiru are brothers.'
>>> stralnum='sugu1234'
>>> print(stralnum.isalnum())
True
>>> stralnum='sugu 1234'
>>> print(stralnum.isalnum())
False
>>> #false because there inbetween sugu and number there is a gap.
>>> string1='Sugumaran'
>>> print(string1.isalpha())
True
>>> string2='Hi Hello'
>>> print(string2.isalpha())
False
>>> string3='Hi1'
>>> string3.isalpha()
False
>>> #decimal
>>> str='sugu'
>>> print('rishi'.capitalize())
Rishi
>>> print('rishik'.upper())
RISHIK
>>> print('SUVE'.lower())
suve
>>> print('SUGU'.islower())
False
>>> print('1234'.isnumeric())
True
>>> print('   '.iswhitespace())
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#57>", line 1, in <module>
AttributeError: 'str' object has no attribute 'iswhitespace'
>>> print('   '.isspace())
True
>>> print('su   '.isprintable())
True
>>> print("    ".isprintable())
True
>>> list=['s''u''g''u']
>>> str2=''
>>> print(str2.join(list))
sugu
>>> str3='    sugu'
>>> print(str3.lstrip)
<built-in method lstrip of str object at 0x7f63ca3a1df0>
>>> print(str3.lstrip())
sugu
>>> str3.ljust(10,'*')
'    sugu**'
>>> 'Thiru'.ljust(10,'+')
'Thiru+++++'
>>> 'C is programming language'.replace('C','Python')
'Python is programming language'
>>> 'Java is easy to learn in Javatpoint'.rfind('Java')
25
>>> 'Ramalingam'.rfind('m',0,4)
2
>>> 'Rathish'.rfind('A',0,5)
-1
>>> 'SelvaKannan'.rindex('K')
5
>>> 'SelvaKannan'.rindex('x')
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#74>", line 1, in <module>
ValueError: substring not found
>>> 'Java is a programmming language'.rsplit('a')
['J', 'v', ' is ', ' progr', 'mmming l', 'ngu', 'ge']
>>> Java is a programmming language'.rsplit('a',1)
SyntaxError: invalid syntax
>>> 'Java is a programmming language'.rsplit('a',1)
['Java is a programmming langu', 'ge']
>>> str5='Python is easy to learn'
>>> str5.startswith('eas',11)
False
>>> str5.startswith('Python')
True
>>> str5.startswith('ea',9)
False
>>> str5.startswith('is',7,10)
True
>>> str5.startswith('is',7)
True
>>> str5.startswith('easy',9)
False
>>> str5[9]
' '
>>> str5[8]
's'
>>> str5.startswith('easy',10)
True
>>> str6='SuGuMaRaN'
>>> str6.swapcase()
'sUgUmArAn'
>>> 