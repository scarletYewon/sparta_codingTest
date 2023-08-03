def solution(phone_number):
  pn = list(phone_number)
  answer = ["*"]*len(pn)
  for i in range(4):
      answer[-(i+1)] = pn[-(i+1)]
  answer = "".join(answer)
  return answer