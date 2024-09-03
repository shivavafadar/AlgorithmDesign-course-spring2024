def winner(n, k, array):
    dp = [False] * (k + 1)
    dp[0] = False
   
    for i in range(1, k + 1):
        for x in array:
            if x <= i and not dp[i - x]:
                dp[i] = True
                break
    
    return "First" if dp[k] else "Second"

n, k = map(int, input().split())
array = list(map(int, input().split()))

print(winner(n, k, array))
