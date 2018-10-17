#!/usr/bin/env python3
import math
import sys
from collections import defaultdict

words_count = defaultdict(lambda : 0)
all_count = 0
with open(sys.argv[1],"r") as f:
  for line in f:
    line = line.replace('\n',' </s>')
    for key in line.split(' '):
      words_count[key] += 1
      all_count += 1

with open('01-train-answer.txt','w') as f:
  for key,value in sorted(words_count.items()):
    f.write("%s\t%f\n" % (key,float(value)/all_count))
  
