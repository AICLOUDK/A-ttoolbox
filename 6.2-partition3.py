from sys import stdin

def partition3(values):
    total_sum = sum(values)
    if total_sum % 3 != 0:
        return 0
    target = total_sum // 3
    n = len(values)
    dp = [0] * (target + 1)
    dp[0] = 1

    for value in values:
        for j in range(target, value - 1, -1):
            dp[j] += dp[j - value]
    
    return 1 if dp[target] >= 3 else 0

if __name__ == '__main__':
    input_n, *input_values = list(map(int, stdin.read().split()))
    assert input_n == len(input_values)
    
    print(partition3(input_values))
