x=18
if(x>=18):
    print('He is eligible for voting')
else:
    print('he is not eligible for voting')
#nested if
player='Dhoni'
if(player=='Virat'):
    print('He is the captain')
elif(player=='Rohit'):
    print('He is opener')
elif(player=='Dhoni'):
    print('He is a wk')
else:
    print('He is an umpire')

#Shorthand if and else
a=20
b=10
if a>b :print('A')
#Shorthand else
a=30
b=50
print('A is greater') if a>b else print('B is greater')

#if we no need to write any content in if we can use pass

s=20
t=3
if(s>t):
    pass
    print('hoi')
elif(t>s):
   pass
else:
    pass
