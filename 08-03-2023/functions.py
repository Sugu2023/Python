#creating function
def demofunction():
    print('Function is called')
demofunction()
print('-------------------------------------------------------')

#arguments
def showingname(name):
    print('Name is',name)
showingname('Suvedha')
showingname('Sugumaran')
print('-------------------------------------------------------')

#arbitary arguments(multiple arguments)
def arbitarg(*args):
    print(args[2])
arbitarg('Sugu','Suve','Thiru','Kokila')
print('-------------------------------------------------------')

#keyword arguments
def keywordarguments(child1,child2,child3):
       print(child3)
keywordarguments(child1='Rathish',child2='Resh',child3='oiu')
print('-------------------------------------------------------')

#arbitary keyword arguments
def arbitarykeyword(**args):
    print('His last name is',args['lname'])
arbitarykeyword(fname='Thiru',lname='Murugan')
print('-------------------------------------------------------')
#default parameter value
def defaultval(country='India'):
  print('Country name',country)
defaultval('SRILANKA')
defaultval('AUSTRALIA')
defaultval()
defaultval('ENGLAND')
print('-------------------------------------------------------')

#passing list as arguments
def listfun(fruit):
    for x in fruit:
        print(x)

fruits=['apple','orange','grapes']
listfun(fruits)
print('-------------------------------------------------------')

#return  values

def factor(n):
    if(n==1):
        return 1
    else:
        return n*factor(n-1)
print(factor(1))

#empty function()---Function  be empty
def emptyfunction():
    pass
emptyfunction()
print('-----------------------------------------------------------')
def fib(n):
    a,b=0,1
    while a<n:
        print(a,end=' ')
        a,b=b,a+b
    print()
fib(10)

def fact(n):
    factorial=1
    if(n<1):
        print('1')
    else:
        for i in range(1,n+1):
            factorial=factorial*i
        print('The factorial of the',n,'is',factorial,'.')
fact(5)
print('-----------------------------------------------------------------------')

#Lambda functions
x=lambda a:a+10
print(x(10))

y=lambda a,b:a*b
print(y(10,3))

#function inside lambda

def myfun(n):
    return lambda a:a*n
mytripler=myfun(3)
print(mytripler(10))
