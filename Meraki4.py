numbers=[56,40,23,70,50,12,5,10,7]
i=0
max=numbers[0]
sec_max=numbers[0]
while i<len(numbers):
    if max<numbers[i]:
        max=numbers[i]
    if numbers[i]<max and numbers[i]>sec_max:
        sec_max=numbers[i]
    i+=1
print(max)
print(sec_max)
        