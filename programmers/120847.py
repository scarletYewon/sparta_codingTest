def solution(numbers):
  num1 = max(numbers)
  numbers.remove(num1)
  num2 = max(numbers)
  answer = num1 * num2
  return answer