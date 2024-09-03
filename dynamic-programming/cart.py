def count_mean(n, x, cards):
    max_sum = n * x 
    dp = [[0 for _ in range(max_sum + 1)] for _ in range(n + 1)]
    dp[0][0] = 1 

    for card in cards:
        for i in range(n, 0, -1):
            for j in range(max_sum, card - 1, -1):
                dp[i][j] += dp[i-1][j-card]
    
    count = 0
    for k in range(1, n+1):
        if k * x <= max_sum:
            count += dp[k][k * x]

    return count

n, x = map(int, input().split())
cards = list(map(int, input().split()))
print(count_mean(n, x, cards))
