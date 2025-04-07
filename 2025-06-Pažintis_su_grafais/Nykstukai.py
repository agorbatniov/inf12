from collections import deque
from typing import List

# Constants (would normally be defined based on problem constraints)
MAXN = 1000  # maximum number of rooms (graph vertices)
MAXK = 1000  # maximum number of dwarves

class DwarvesSolution:
    def __init__(self):
        self.n = 0                  # number of rooms (vertices)
        self.adj = [[] for _ in range(MAXN)]  # adjacency list
        self.nykSk = 0              # number of dwarves
        self.kamb = [0] * MAXK      # kamb[i] = room number of i-th dwarf
        self.isejimas = 0           # exit room number
        self.t = 0                  # time limit
        self.spes = [False] * MAXK  # which dwarves can make it
        self.atstumas = [0] * MAXN  # distances from exit

    def bfs(self, p: int):
        """Perform BFS starting from room p to calculate distances"""
        q = deque()
        # Initialize distances to -1 (unvisited)
        self.atstumas = [-1] * MAXN
        
        # Start with the exit room
        self.atstumas[p] = 0
        q.append(p)

        while q:
            v = q.popleft()
            for u in self.adj[v]:
                # If neighbor hasn't been visited
                if self.atstumas[u] == -1:
                    self.atstumas[u] = self.atstumas[v] + 1
                    q.append(u)

    def kasSpes(self):
        """Determine which dwarves can reach the exit in time"""
        self.bfs(self.isejimas)
        for i in range(self.nykSk):
            self.spes[i] = self.atstumas[self.kamb[i]] <= self.t

    def read_input_and_solve(self):
        """Example method to read input and solve the problem"""
        # In a real scenario, this would read from input files or stdin
        # Here's just a template of how it might work
        
        # Read graph information
        self.n = int(input("Enter number of rooms: "))
        edge_count = int(input("Enter number of doors: "))
        
        print("Enter door connections (room1 room2):")
        for _ in range(edge_count):
            u, v = map(int, input().split())
            self.adj[u].append(v)
            self.adj[v].append(u)  # assuming doors are bidirectional
            
        # Read dwarves information
        self.nykSk = int(input("Enter number of dwarves: "))
        print("Enter room numbers for each dwarf:")
        self.kamb = list(map(int, input().split()))
        
        # Read exit and time limit
        self.isejimas = int(input("Enter exit room number: "))
        self.t = int(input("Enter time limit: "))
        
        # Solve
        self.kasSpes()
        
        # Output results
        print("Dwarves who can make it:")
        for i in range(self.nykSk):
            if self.spes[i]:
                print(f"Dwarf {i+1} (room {self.kamb[i]})")

# Example usage
if __name__ == "__main__":
    solution = DwarvesSolution()
    
    # For actual problem solving, you would use:
    # solution.read_input_and_solve()
    
    # Here's a quick test case
    solution.n = 5
    solution.adj = [[], [2, 3], [1, 4], [1, 4], [2, 3, 5], [4]]  # 1-based indexing
    solution.nykSk = 3
    solution.kamb = [1, 3, 5]  # dwarves in rooms 1, 3, 5
    solution.isejimas = 1       # exit is room 1
    solution.t = 2              # time limit is 2
    
    solution.kasSpes()
    print("Test results:")
    for i in range(solution.nykSk):
        print(f"Dwarf {i+1}: {'Yes' if solution.spes[i] else 'No'}")