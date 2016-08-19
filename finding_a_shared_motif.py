f = open('rosalind_lcsm.txt','r')
fdata = f.read()
f.close()

keys, v = zip(*[x.split('\n',1) for x in fdata.split('>')[1:]])
vals = [y.replace('\n', '') for y in v]
d = dict(zip(vals,keys))

# use the shortest string as the reference
ref = vals[[len(x) for x in vals].index(min([len(x) for x in vals]))]

for j in range(1,len(ref)):
  for i in range(0, j+1):
    # take a substring and test it against the others
    test = ref[0+i:len(ref)-j+i]
    if False not in [test in x for x in vals]:
      print test
      break
  else:
    continue  # executed if the loop ended normally (no break)
  break  # executed if 'continue' was skipped (break)
