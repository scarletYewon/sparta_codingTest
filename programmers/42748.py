def solution(array, commands):
    answer = []
    sets = []
    for i in commands:
        sets.append(array[i[0]-1:i[1]])
    print(sets)
    for i in range(len(sets)):
      sets[i].sort()
    print(sets)
    for i in range(len(commands)):
      answer.append(sets[i][commands[i][2]-1])
    print(answer)
    return answer