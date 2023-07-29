def solution(id_pw, db):
  answer = ''
  ID = id_pw[0]
  PW = id_pw[1]
  
  for i in db:
      if i[0] == ID:
          if i[1] == PW:
              answer = "login"
              break
          else:
              answer = "wrong pw"
              break
      else:
          answer = "fail"  
  return answer