def faktorialas(n):
           if n == 0:
               return 1
           else:
               return n * faktorialas(n-1)

factor = faktorialas(5)
print(factor)