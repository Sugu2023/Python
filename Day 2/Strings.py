Python 3.8.10 (default, Nov 14 2022, 12:59:47) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=10/2
>>> b=100
>>> b*a
500.0
>>> b+_
600.0
>>> b+_
700.0
>>> round(_,2)
700.0
>>> b=200
>>> b
200
>>> b+_
400
>>> b
200
>>> b+_
400
>>> b+_
600
>>> b
200
>>> #Strings
>>> 'Sugu' 'Thiru'
'SuguThiru'
>>> 'Sugu Maran' #single quotes
'Sugu Maran'
>>> 'You should\'nt do this ' #use \' to escape the single quotes
"You should'nt do this "
>>> '"Yes," they said this'
'"Yes," they said this'
>>> print('SUgu')
SUgu
>>> print('Is\'nt they said')
Is'nt they said
>>> s='First line.\n Second Line'
>>> s
'First line.\n Second Line'
>>> #without print if we use \n ,that will be included in the output.
>>> print(s)#using print we can overcome that
First line.
 Second Line
>>> #if we need  to use \ as character then include r before the first quote.
>>> print('c:\some\name')
c:\some
ame
>>> print(r'c:\desk\name\file')
c:\desk\name\file
>>> #string literals can span multiple lines
>>> '''\ Hi             hello
Say: Good Morning to all
Greet: With a smilev'''
'\\ Hi             hello\nSay: Good Morning to all\nGreet: With a smilev'
>>> print('''\ Hi             hello
Say: Good Morning to all
Greet: With a smilev''')
\ Hi             hello
Say: Good Morning to all
Greet: With a smilev
>>> #String can concated using + and repeated using *
>>> print('selva' + 'kanan')
selvakanan
>>> print(2*'Suve')
SuveSuve
>>> #two or more string literals next to each other are automatically concatenated.
>>> 'HTML' '&' 'css'
'HTML&css'
>>> 'html' '&'   'css'
'html&css'
>>> #above feature only works with two string literals but not with two variables.
>>> s='py'
>>> y='thon'
>>> print(s y)
SyntaxError: invalid syntax
>>> print(s+y)
python
>>> #two varibales can be concatenated by using +operator.
>>> #String can be indexed with first character having index 0.
>>> word='Sentence'
>>> word[2]
'n'
>>> #we can give negative indices also
>>> word[-2]#it prints the character from last second position.
'c'
>>> #Slicing is used to obtain substring.
>>> word[0:4]
'Sent'
>>> word[-1:-5]
''
>>> word[2:]
'ntence'
>>> word[:2]+word[2:]
'Sentence'
>>> #in slicing if start index is omited then it defaults to 0 and when the end index is vomitted then it defaults to size of the string.
>>> word[0:]
'Sentence'
>>> word[:4]
'Sent'
>>> #outof range indices are handled perfectly
>>> word[4:43]
'ence'
>>> word[33:4]
''
>>> #In python strings are immutable and can be reassigned again.
>>> word[1]='k'
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#61>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> #but if we need new one we can create
>>> 'd]+word[1:]
SyntaxError: EOL while scanning string literal
>>> 'd'+word[1:]
'dentence'
>>> sent='Fog'
>>> 'D'+sent[0:]
'DFog'
>>> 'D'+sent[1:]
'Dog'
>>> 'ad'+sent[:2]
'adFo'
>>> 'ad'+sent[2:3]
'adg'
>>> #using len() we can find the length of the string.
>>> alpha='abcdefghijklmnopqurstuvwxyz'
>>> len(alpha)
27
>>> s='sugu'
>>> s.capitalize()
'Sugu'
>>> 
