stmarks=[90,'A',34,34,'A',34,'A',76]
stmarks1=[]
for i in stmarks:
    if (i!='A'):
        stmarks1.append(i)
for i in range(len(stmarks1),len(stmarks)):
    stmarks1.append('A')
print(stmarks)
print(stmarks1)       