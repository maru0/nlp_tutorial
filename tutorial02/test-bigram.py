#!/usr/bin/python3
import sys
import math
from collections import defaultdict

lam1 = 0.95
lam2 = 0.95
V = 10 ** 6
W = 0
H = 0
words = defaultdict(lambda : 0)
with open(sys.argv[1],"r") as f:
  for line in f:
    line = line.split('\t')
    print(line)
    words[line[0]] = float(line[1])

with open(sys.argv[1],"r") as f:
  for line in f:
    words_list = line.split()
    words_list.append('</s>')
    words_list.insert(0,'<s>')
    for i in range(1,len(words_list)):
      p1 = lam1 * words[words_list[i]] + (1-lam1) / V
      p2 = lam2 * words[words_list[i-1]+' '+words_list[i]] + (1-lam2) * p1
      H += -math.log(2,p2)
      W += 1
  print(H/W)
