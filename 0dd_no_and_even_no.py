# elements=[23,14,56,12,19,9,15,25,31,42,43]
# i=0
# while i<len(elements):
#     if elements[i]%2==0:
#         print("even nuber")
#     else:
#         print("odd no.") 
#     i+=0       

elements=[23,14,56,12,19,9,15,25,31,42,43]
i=0
c1=0
c=0
a=[]
b=[]
while i <len(elements):
    if elements[i]%2==0:
        c1+=1
        a.append(elements[i])
    elif elements[i] %2!=0:
        c+=1
        a.append(elements[i])
    i=i+1
    print("even",c1)
    print("odd", c)    
           