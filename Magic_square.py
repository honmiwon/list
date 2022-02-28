magic_square=[
    [8,3,4],
    [1,5,9],
    [6,7,2]
]

row=0
col=0
dig=0            
i=0
while i<len(magic_square):
    j=0
    while j<len(magic_square):
        row=row+magic_square[i][j]
        col=col+magic_square[j][i]
        dig=dig+magic_square[j][j]
        j+=1
    i+=1
print(row)
print(col)
print(dig)
if row==col==dig:  
    print(magic_square)                           