#!/usr/bin/python3
import sys
import math
from collections import defaultdict

all_counts = 0
counts = defaultdict(lambda : 0)
n_counts = defaultdict(lambda : 0)
with open(sys.argv[1],"r") as f:
  for line in f:
    words = line.split()
    words.append("</s>")
    words.insert(0,"<s>")
    for i in range(1,len(words)):
      counts[ words[i-1]+' '+words[i] ] += 1
      counts[words[i]] += 1
      n_counts[words[i-1]] += 1
      all_counts += 1

#print(counts)
#print(n_counts)
with open(sys.argv[2],"w") as f:
  for count in sorted(counts.keys()):
    count_se = count.split()
    if len(count_se) >= 2:
      deno = n_counts[count_se[0]]
    else:
      deno = all_counts
    #print(count_se,deno)
    prb = float(counts[count] / deno)
    print(count,prb)
    f.write("{}\t{}\n".format(count,prb))
