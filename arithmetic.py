def hyp(x, y):
  return x**2 + y**2

f = open('rosalind_ini2.txt', 'r')
a, b = map(int, f.read().split())
f.close()

print hyp(a, b)
