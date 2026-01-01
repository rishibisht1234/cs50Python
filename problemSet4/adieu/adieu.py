import inflect

p=inflect.engine()
names=[]
while True:
    try:
        name=input('Name: ')
        names.append(name)
    except EOFError:
        break

output='Adieu, adieu, to '+p.join(names)
print()
print(output)


