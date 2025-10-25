def count_dice_ways(n):
    MOD = 10 ** 9 + 7

    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        for dice in range(1, 7):
            if i - dice >= 0:
                dp[i] = (dp[i] + dp[i - dice]) % MOD
    return dp[n]

n = int(input())
result = count_dice_ways(n)
print(result)