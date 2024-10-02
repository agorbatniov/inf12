from collections import deque

stack = deque()

# Pridėjimas ir pašalinimas naudojant deque
stack.append(10)
stack.append(20)
stack.pop()    # Pašalina paskutinį elementą (20)
stack.pop()    # Pašalina paskutinį elementą (10)
