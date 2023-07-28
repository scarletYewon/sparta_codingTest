def solution(num, total):
  s = sum(range(1, num))
  start = (total - s) // num
  answer = [i for i in range(start, start+num)]
  return answer