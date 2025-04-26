from sys import stdin

def max_weight(capacity, weights):
    m = [0] * (capacity + 1)
    for weight in weights:
        for cap in range(capacity, weight - 1, -1):
            m[cap] = max(m[cap], m[cap - weight] + weight)
    return m[capacity]

if __name__ == '__main__':
    capacity, n, *weights = map(int, stdin.read().split())
    print(max_weight(capacity, weights))