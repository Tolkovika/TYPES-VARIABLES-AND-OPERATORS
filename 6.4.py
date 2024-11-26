employee = "Mr. John May, born on 1998-02-16"

name = employee[4:8]  
surname = employee[9:12]  
born = employee[22:32]  
initials = f'{name[0]}.{surname[0]}.'  

print(f'Name: {name}')
print(f'Surname: {surname}')
print(f'Born: {born}')
print(f'Initials: {initials}')
