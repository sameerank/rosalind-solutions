# Computing Hamming distance

fin = open('rosalind_hamm.txt','r')
data = fin.read()
fin.close()

[s, t] = data.split('\n')[:2]

c = 0
for i in range(len(s)):
  if s[i] != t[i]:
    c += 1

print(c)
