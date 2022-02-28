numbers=[1,4,2,10]
i=0
max=numbers[0]
while i<len(numbers):
    if numbers[i]>max:
        max=numbers[i]
    i+=1
print(max)        