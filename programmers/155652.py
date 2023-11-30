def solution(s, skip, index):
  answer = ""
  alpha = "abcdefghijklmnopqrstuvwxyz"
  
  for ch in skip:
    if ch in alpha:
      alpha = alpha.replace(ch, "") # 알파벳 안에 skip 문자들 제거
          
  for i in s:
    # s의 문자 인덱스 + index를 alpha의 길이로 나눈 나머지를 알파벳으로 변환
    change = alpha[(alpha.index(i) + index) % len(alpha)] 
    answer += change
      
  return answer