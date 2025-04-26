def majority_element(elements):
    counts = {}
    for i in elements:
        counts[i] = counts.get(i, 0) + 1
        if counts[i] > len(elements) // 2:
            return 1
    return 0

if __name__ == '__main__':
    input()
    input_elements = list(map(int, input().split()))
    print(majority_element(input_elements))
