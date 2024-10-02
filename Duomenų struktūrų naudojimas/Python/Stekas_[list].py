# Naudojame list kaip steką
stack = []

# Pridedame elementus į steką
stack.append(10)
stack.append(20)

# Pašaliname elementus iš steko
print(stack.pop())  # Pašalina ir išveda paskutinį elementą (20)
print(stack.pop())  # Pašalina ir išveda paskutinį elementą (10)

# Patikriname, ar stekas tuščias
if not stack:
    print("Stekas yra tuščias")
