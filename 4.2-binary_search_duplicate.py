def binary_search(keys, query):
    left, right, result = 0, len(keys) - 1, -1
    while left <= right:
        mid = (left + right) // 2
        if keys[mid] == query:
            result, right = mid, mid - 1
        elif keys[mid] < query:
            left = mid + 1
        else:
            right = mid - 1
    return result

if __name__ == '__main__':
    input()
    input_keys = list(map(int, input().split()))
    input()
    input_queries = list(map(int, input().split()))
    print(' '.join(str(binary_search(input_keys, q)) for q in input_queries))
