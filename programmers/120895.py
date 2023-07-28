def solution(my_string, num1, num2):
  answer = ''
  ex = list(my_string)
  ex[num1],ex[num2] = ex[num2],ex[num1]
  answer = ''.join(ex)
  return answer
