def solution(my_string):
  answer = ''
  for i in list(my_string):
      if i in answer:
          continue
      else:
          answer +=i
  return answer