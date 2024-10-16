# Viršūnių sąrašas (vertices)
vertices = ['A', 'B', 'C', 'D', 'E']

# Briaunų sąrašas su svoriais (edges)
edges = [
    ('A', 'B', 4),
    ('A', 'C', 2),
    ('B', 'C', 5),
    ('B', 'D', 10),
    ('C', 'E', 3),
    ('D', 'E', 1)
]

# Grafo atvaizdavimas: viršūnių ir briaunų su svoriais sąrašai
print("Viršūnių sąrašas:", vertices)
print("Briaunų sąrašas (pradinis taškas, galutinis taškas, svoris):")
for edge in edges:
    print(f"{edge[0]} -> {edge[1]} (svoris: {edge[2]})")
