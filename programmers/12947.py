def solution(x):
  X = list(str(x))
  sum = 0
  for i in range(len(X)):
    sum += int(X[i])
  if x%sum ==0:
    return True
  return False