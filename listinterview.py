list=[[1,2,3],[4,5,6],[7,8,9]]
i=0
a=0
b=0
c=0
while i<len(list):
    a=a+list[i][0]
    b=b+list[i][0]
    c=c+list[i][0]
    i=i+1
    print(a,b,c)
if a==b==c:
    print("list")
else:
    print("not a list")    
    