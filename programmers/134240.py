def solution(food):
    l = ''
    for i in range(len(food)-1):
        if food[i+1] %2==1:
            food[i+1] -=1
        
    for i in range(len(food)-1):
        l+=(str(i+1)*(food[i+1]//2))
    
    answer = l+'0'+l[::-1]
    return answer