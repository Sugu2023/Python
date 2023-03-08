#for statements
players=['Virat','Rohit','SKY','Jaddu','Dhoni']
for x in players:
    print(x)
bikes=('r15','rx100','boxer')
for y in bikes:
    print(y)
thisdict=dict(name='Sugu',age=21,location='Elandhai')
for z in thisdict.keys():
    print(z)
for a in thisdict.values():
        print(a)
#loop in string
str1='Sugumaran'
for b in str1:
     print(b)

#break statement
str2='Ramalingam'
for c in str2:
     print(c)
     if c=='i':
      break
#continue

str3='Thirumurugan'
for d in str3:
    
    if(d=='m'):
        continue
    print(d)

#range function()
for x in range(6):
    print(x)

#parameters
for y in range(2,10):
    print(y)
for z in range(1,10,2):
    print(z)

#else in loop
for g in range(2,20,2):
    print(g)
else:
    print('Loop is finished')
#else is not executed if the loop is terminated by break.

#nested loops
players=['Dhoni','Virat','Rohit','Jaddu','KL']
nick=['Thala','King','Hitman','Warrior','Classy']
for x in players:
    for y in nick:
        print(x,y)
