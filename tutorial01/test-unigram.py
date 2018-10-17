#!/usr/bin/env python3
import sys
import math
from collections import defaultdict

# Parameters
N = 10 ** 6
lam_unk = 0.05
lam = 1-lam_unk
H = w_count = w_unk = 0
# global variable
prob = {}
words_count = defaultdict(lambda : 0)
all_count = 0

def word_match(key):
  global H,w_count,w_unk
  w_count += 1
  if key in prob:
    P = lam * prob[key] + lam_unk / N
  else:
    w_unk += 1
    P = lam * 0 + lam_unk / N
  H += -1 * math.log(P,2)
  return (H,w_count,w_unk)

with open(sys.argv[1],"r") as f:
  for line in f:
    line = line.strip().split("\t")
    prob[line.pop(0)] = float(line.pop(1))

with open(sys.argv[2],"r") as f:
  for line in f:
    line = line.replace('\n',' </s>')
    for key_line in line.split(' '):
      H,w_count,w_unk = word_match(key_line)
  print(H/w_count)
  print((w_count - w_unk)/w_count)

