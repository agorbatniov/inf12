import heapq

def dijkstra(graph, start):
    # Inicializuojame atstumus su begalybe
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    
    # Naudojame priority queue (min-heap)
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Tikriname, ar atstumas yra didesnis nei jau žinomas
        if current_distance > distances[current_vertex]:
            continue
        
        # Patikriname kaimyninius vertexus
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            # Atnaujiname atstumą, jei randame trumpesnį
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# Pavyzdinis grafas (kaimynų sąrašas su svoriais)
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'C': 5, 'D': 10},
    'C': {'E': 3},
    'D': {'E': 1},
    'E': {}
}

# Iškviečiame Dijkstra's algoritmą
start_vertex = 'A'
shortest_paths = dijkstra(graph, start_vertex)
print("Trumpiausi keliai nuo", start_vertex, ":", shortest_paths)
