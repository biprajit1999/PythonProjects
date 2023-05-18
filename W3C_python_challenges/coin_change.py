# def change(self, amount: int, coins: List[int]) -> int:
def change(amount,coins):
    dp = [0] * (amount + 1)
    dp[0] = 1

    for coin in coins:
        for v in range(1, amount + 1):
            if v - coin >= 0:
                dp[v] += dp[v - coin]

    for i in dp:
        print(i,end=" ")
    print()
    return dp[amount]


amt = 5
coins = [1,2,5]

print(change(amt,coins))
