def solution(arr1, arr2):
  answer = []
  ex=[]
  for i in range(len(arr1)):
    for j in range(len(arr1[0])):
      ex.append(arr1[i][j]+arr2[i][j])
    answer+=[ex]
    ex = []
  return answer