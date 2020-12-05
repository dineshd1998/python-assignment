months={"Jan":11,"Feb":12,"Mar":1,"Apr":2,"May":3,"Jun":4,"Jul":5,"Aug":6,"Sep":7,"Oct":8,"Nov":9,"Dec":10}
m=input("Enter a Date")
listt=m.split(' ')
d=int(listt[0])
m=months[listt[1]]
Yr=listt[2]
y=int(Yr[:2])
c=int(Yr[2:])
'''
Formula --> w=(d+|2.6*m-0.2|+y+|y/4|+|c/4|-2c)mod 7
'''
term=round((2.6*m-0.2)%7)
print(term)


