f = open('rosalind_iev.txt', 'r')
nums = f.readline()
f.close()

def expected(cn):
  return cn[0]*2 + cn[1]*2 + cn[2]*2 + cn[3]*1.5 + cn[4]*1 + cn[5]*0
  
intn = [int(n) for n in nums.split()]
print expected(intn)
