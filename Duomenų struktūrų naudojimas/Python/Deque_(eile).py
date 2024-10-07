from collections import deque

# Sukuriame eilę
queue = deque()

# Pridedame elementus (enqueue)
queue.append("Element 1")
queue.append("Element 2")

# Pašaliname elementą (dequeue)
first = queue.popleft()

# Peržiūrime pirmą elementą
peek_element = queue[0]

print(f"Pirmas elementas: {peek_element}")
