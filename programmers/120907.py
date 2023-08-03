def solution(quiz):
  answer = []
  list = []
  for i in quiz:
    list = i.split(" ")
    num1,ques,num2,ans = list[0],list[1],list[2],list[4]
    if ques == "+":
      if int(num1) + int(num2) == int(ans):
        answer.append("O")
      else:
        answer.append("X")
    else:
      if int(num1) - int(num2) == int(ans):
        answer.append("O")
      else:
        answer.append("X")
  return answer