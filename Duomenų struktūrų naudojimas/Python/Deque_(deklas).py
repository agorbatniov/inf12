from collections import deque

# Sukuriame tuščią deklą
d = deque()

# Pridedame elementus į galą ir į priekį
d.append(10)       # Prideda į galą
d.appendleft(20)   # Prideda į priekį

# Pašaliname elementus iš galo ir priekio
d.pop()            # Pašalina iš galo
d.popleft()        # Pašalina iš priekio

print(d)  # Išveda deque([])