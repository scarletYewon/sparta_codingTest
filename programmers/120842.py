def solution(num_list, n):
  answer = []
  cnt = 0
  answer_ = []
  for i in num_list:
      answer_.append(i)
      cnt += 1
      if cnt == n:
          answer.append(answer_)
          answer_ = []
          cnt = 0

  return answer