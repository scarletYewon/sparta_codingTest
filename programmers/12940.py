import math

def solution(n, m):
  answer = [math.gcd(n,m),lcm(n,m)]
  return answer

# 프로그래머스에서 math.lcm이 안돼서 그냥 만듦
def lcm(n,m):
  return (n*m) // math.gcd(n,m)