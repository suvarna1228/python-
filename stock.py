
def maxProfit(a):
    maxPro = 0
    minPrice = float('inf')
    for i in range(len(a)):
        minPrice = min(minPrice, a[i])
        maxPro = max(maxPro, a[i] - minPrice)
    return maxPro

a = [7, 1, 5, 3, 6, 4]
maxPro = maxProfit(a)
print("Max profit is:", maxPro)