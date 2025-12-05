l = [1,0,2,3,4,0]

cnt = 0 
nl = []
for i in l:
    if i == 0:
        cnt +=1
    else:
        nl.append(i)

fl = nl + [0] * cnt

print(nl)
print(fl)

