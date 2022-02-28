magic_square=[
    [8,3,4],
    [1,5,9],
    [6,7,2]
    
]
i=0
sr=0
sc=0
while i<len(magic_square):
    j=0
    sc=sc+magic_square[i][j]
    sr=sr+magic_square[j][i]
    i=i+1
print(sr)
print(sc) 
c=0
d=0
f=(len(magic_square)-1)
d1=0
d2=0
while c<len(magic_square):
    d1=d1+magic_square[c] [d]
    d2=d2+magic_square[c][f]
    c+=1
    d+=1
    f-+1
print(d1)
print(d2) 
if sc==sr==d1==d2:
    print("magic_square") 
else:
    print("not a magic_square")          