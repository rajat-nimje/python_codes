l = [1,0,2,3,4,0]

largest = float('-inf')
second = float('-inf')

for i in l:
    if i> largest:
        second = largest
        largest = i
    elif (largest >i ) & (i>second):
        second = i

print(second)
print(largest)