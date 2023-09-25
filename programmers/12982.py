def solution(d, budget):
    answer = 0
    s = 0
    d.sort()
    for i in d:
        s += i
        if s > budget:
            break
        else:
            answer +=1
    return answer