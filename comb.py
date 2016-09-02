# Given: Two DNA strings s and t (each of length at most 1 kbp).
# Return: All locations of t as a substring of s.
# Sample Dataset
# GATATATGCATATACTT
# ATAT
# Sample Output
# 2 4 10

def comb(s, t):
  lc = []
  nf = 0
  while s.find(t, nf) != -1:
    nf = s.find(t, nf)
    nf += 1
    lc.append(str(nf))
  return " ".join(lc)
    
fin = open('rosalind_subs.txt', 'r')
sin = fin.readline().rstrip('\n')
tin = fin.readline().rstrip('\n')
fin.close()


print comb(sin, tin)
