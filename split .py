list=["a","b","c","d","e","f","g","h","i","j","k","l","m","n"]
list1=[]
step=3
i=0
while i<step:
    list1.append(list[i::step])
    i+=1
print(list1)