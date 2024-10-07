l = []

for i in range(5):
    print('Enter %i element'%i)
    l.append(int(input()))
l.sort()
minsum,maxsum =0,0
for i in range(5):
    print(l[i])

    if l[i] != l[0]:
        maxsum = maxsum + l[i]

    if l[i] != l[4]:
        minsum = minsum + l[i]

print(maxsum, minsum)
print("Thanks")


    



 








