b=[1,0,0,1,1,0,1,1,]
i=len(b)-1
power=0
a=1
while i>=0:
    power=power+int(b[i]/a)
    a=a/2
    i-=1
print(power) 