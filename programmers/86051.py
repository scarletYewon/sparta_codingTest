def solution(numbers):
  nonlist = []
  for i in range(10):
      if i in numbers:
          continue
      else:
          nonlist.append(i)
          
  answer = sum(nonlist)
  return answer