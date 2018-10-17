#!/usr/bin/env python3

import sys
from collections import defaultdict

count_dict = defaultdict(lambda : 0)
with open(sys.argv[1],"r") as f:
  for line in f:
    for key in line.strip().split(' '):
      count_dict[key] += 1

with open("answer.txt","a") as f:
  for ans,wer in sorted(count_dict.items()):
    f.write("%s\t%s\n" % (ans,wer))
