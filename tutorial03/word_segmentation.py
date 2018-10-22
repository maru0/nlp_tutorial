#!/usr/bin/python3
import sys
import math
from collections import defaultdict

def train_unigram(input_file,model_file):
  counts = defaultdict(lambda : 0)
  total_count = 0
  with open(input_file,"r") as f:
    for line in f:
      words = line.split()
      words.append("</s>")
      for word in words:
        counts[word] += 1
        total_count += 1
  with open(model_file,"w") as f:
    for word in counts.keys():
      prob = float(counts[word])/total_count
      f.write(word+"\t"+str(prob)+"\n")

def viterbi(model,test,answer):
  N = 10 ** 6
  lam = 0.95
  probs = defaultdict(lambda : 0)
  with open(model,"r",encoding='utf-8') as f:
    for line in f:
      line = line.split()
      probs[line[0]] = float(line[1])
  # アルゴリズムの処理
  with open(test,"r",encoding='utf-8') as f,open(answer,"w") as ans:
    for line in f:
      line = line.strip('\n')
      best_edge = dict()
      best_score = dict()
      best_edge[0] = 'NULL'
      best_score[0] = 0
      for word_end in range(1,len(line)+1):
        best_score[word_end] = 10**10
        for word_begin in range(0,len(line)):
          word = line[word_begin:word_end]
          # 未知語でなく、1-gram
          if word in probs.keys() or len(word) == 1:
            prob = lam * probs[word] + (1-lam) / N
            my_score = best_score[word_begin] - math.log(prob,2)
            if my_score < best_score[word_end]:
              best_score[word_end] = my_score
              best_edge[word_end] = (word_begin,word_end)
      print(best_edge)
      print(best_score)
      words = []
      next_edge = best_edge[len(best_edge)-1]
      while next_edge != 'NULL':
        word = line[next_edge[0]:next_edge[1]]
        words.append(word)
        next_edge = best_edge[next_edge[0]]
      words.reverse()
      print(''.join(words))
      ans.write(' '.join(words)+'\n')
      
if __name__ == '__main__':
  train_unigram(sys.argv[1],sys.argv[2])
  viterbi(sys.argv[2],sys.argv[3],sys.argv[4])
