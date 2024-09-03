def largest_number(n, allowed_digits):
    segment_count = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}
    allowed_segments = [(digit, segment_count[digit]) for digit in allowed_digits if digit in segment_count]
    dp = ["" if i == 0 else None for i in range(n+1)]

    for i in range(1, n+1):
        for digit, seg in allowed_segments:
            if i >= seg and dp[i - seg] is not None:
                candidate = str(digit) + dp[i - seg]
                if dp[i] is None or (len(candidate) > len(dp[i])) or (len(candidate) == len(dp[i]) and candidate > dp[i]):
                    dp[i] = candidate
    
    return dp[n] if dp[n] is not None else "0"  

n, m = map(int, input().split())
allowed_digits = list(map(int, input().split()))
print(largest_number(n, allowed_digits))
