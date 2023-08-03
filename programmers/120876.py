def solution(lines):
  line = [set(range(min(i), max(i))) for i in lines]
  answer = line[0] & line[1] | line[0] & line[2] | line[1] & line[2]
  return len(answer)