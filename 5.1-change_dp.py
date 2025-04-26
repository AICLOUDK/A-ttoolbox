def change(money):
    coin = [1, 3, 4]
    min_Coin = [float('inf')] * (money + 1)
    min_Coin[0] = 0

    for i in range(1, money + 1):
        for x in coin:
            if i >= x:
                min_Coin[i] = min(min_Coin[i], min_Coin[i - x] + 1)

    return min_Coin[money]

if __name__ == '__main__':
    m = int(input())
    print(change(m))
          
