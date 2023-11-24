def solution(k, m, score):
    s = len(score)
    b = s//m
    ns = []
    cnt=0
    sum = 0
    
    score.sort(reverse=True)
    
    for i in range(b):
        ns.append(score[cnt:cnt+m])
        cnt+=m
    
    for i in range(b):
        sum += min(ns[i])*m
    
    return sum

# def solution(k, m, score):
#   return sum(sorted(score)[len(score)%m::m])*m