# Computing GC content

fin = open('rosalind_gc.txt','r')
data = fin.read()
fin.close()
splitdata = data[1:].split('>')
ids = []
cgcontent = []
for i in splitdata:
  lines = i.split('\n')
  ids.append(lines[0])
  cgdata = "".join(lines[1:])
  cgcontent.append(100*(cgdata.count('C')+cgdata.count('G'))/float(len(cgdata)))
maxi = cgcontent.index(max(cgcontent))

print ids[maxi]
print cgcontent[maxi]
