list=['string','43',3.0,8.9,-4,-2,19,18]
i=0
b=[]
c=[]
d=[]
e=[]
c=[]
while i<len[list]:
    if (type(list[i])==str):
        b.append(list[i])
    elif(type(list[i]==float)):
        c.append(list[i]) 
    elif list[i]>0:
        d.append(list[i]) 
    else:
        e.append(list[i]) 
    i=i+1
print(',"in",c,"\n,"d,"\n,"e')                