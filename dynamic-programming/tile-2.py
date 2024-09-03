def min_cost(tile):
    n = len(tile)
    dp = [[0] * n for _ in range(n)]
    prefix = [0] * n
    prefix[0] = tile[0]

    for i in range(1, n):
        prefix[i] = prefix[i-1] + tile[i]

    for length in range(2, n+1): 
        for i in range(n-length+1):
            j = i + length - 1
            dp[i][j] = float('inf')
            total = prefix[j] - (prefix[i-1] if i > 0 else 0)
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + total
                if cost < dp[i][j]:
                    dp[i][j] = cost

    return dp[0][n-1]

n = int(input())
tile = list(map(int, input().split()))
print(min_cost(tile))
