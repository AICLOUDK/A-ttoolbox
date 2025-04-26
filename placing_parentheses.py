def evaluate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def maximum_value(dataset):
    numbers = []
    operators = []
    
    num = ''
    for char in dataset:
        if char.isdigit():
            num += char
        else:
            numbers.append(int(num))
            operators.append(char)
            num = ''
    numbers.append(int(num))
    
    n = len(numbers)
    min_dp = [[0] * n for _ in range(n)] 
    max_dp = [[0] * n for _ in range(n)]
    
    for i in range(n):
        max_dp[i][i] = numbers[i]
        min_dp[i][i] = numbers[i]
    
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            max_value = float('-inf')
            min_value = float('inf')
            
            for k in range(i, j):
                op = operators[k]
                a = evaluate(max_dp[i][k], max_dp[k + 1][j], op)
                b = evaluate(max_dp[i][k], min_dp[k + 1][j], op)
                c = evaluate(min_dp[i][k], max_dp[k + 1][j], op)
                d = evaluate(min_dp[i][k], min_dp[k + 1][j], op)
                
                max_value = max(max_value, a, b, c, d)
                min_value = min(min_value, a, b, c, d)

            max_dp[i][j] = max_value
            min_dp[i][j] = min_value
            
    return max_dp[0][n - 1]

if __name__ == "__main__":

    print(maximum_value(input().strip()))