import math

def solution(n):
  answer = 0
  for i in range(2,n+1):
    if primenumber(i):
      answer+=1
  return answer

def primenumber(x):
  # 특정한 숫자의 제곱근까지만 약수의 여부를 검증하면 된다
  for i in range(2, int(math.sqrt(x))+1):	
    if x % i == 0:	
      return False
  return True	