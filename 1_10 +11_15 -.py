list=[1,2,3,4,5,6,7,8,9,10,-11,12,13,14,15]
i=0
b=[]
c=[]
sum=0
while i<len(list):
    if list[i]>0:
        c.append([i])
        j=c[0]
        while j<len(c):
            if c[0]:
                j=c[i]
            