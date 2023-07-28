def solution(num, k):
  answer = 0
  n = list(str(num))
  for i in n:
      if i == str(k):
          answer = (n.index(i))+1
  if answer == 0:
      return -1
  return answer