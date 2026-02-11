stmarks=[90,'A',34,34,'A',34,'A']
stmarks1=[]
stmarks2=[]
for i in stmarks:
    if i!='A':
        stmarks1.append(i)
    else:
        stmarks2.append(i)
    stmark=stmarks1+stmarks2
print(stmark)

