#나의 풀이
def solution(nums):
    def DFS(L,sum,c):
        global answer
        if(c>3):
            return 
        if(L==n):
            if(sum%2!=0 and c==3):
                cnt=0
                for m in range(2,sum+1):
                    if(sum%m==0):
                        cnt+=1
                    if(cnt>1):
                        break
                if(cnt==1):
                    answer+=1
                    print(sum)

        else:
            DFS(L+1,sum+nums[L],c+1)
            DFS(L+1,sum,c)

    global answer
    answer= 0
    n=len(nums)
    DFS(0,0,0)
    return answer


#다른 사람의 풀이
def solution(nums):
    from itertools import combinations as cb
    answer = 0
    for a in cb(nums, 3):
        cand = sum(a)
        for j in range(2, cand):
            if cand%j==0:
                break
        else:
            answer += 1
    return answer
