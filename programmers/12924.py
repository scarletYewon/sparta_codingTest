def solution(n):
    cnt = 0
    for i in range(n):
        sum = 0
        for j in range(i+1,n+1):
            sum +=j
            if sum == n:
                cnt+=1
                break
            elif sum>n:
                break
    return cnt

# def solution(n):
#     return len([i  for i in range(1,n+1,2) if n % i is 0])