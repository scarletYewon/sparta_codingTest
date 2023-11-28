from itertools import combinations

def solution(nums):
  cnt = 0
  l = list(combinations(nums,3))
  for i in range(len(l)):
    if is_prime_number(sum(l[i])):
      cnt+=1
  return cnt

def is_prime_number(n):
  for i in range(2, n):
    if n % i == 0:
      return False
  return True