def left_rotation(a,n,k):
  k = k % n
  return a[k:] + a[:k]
k=2
a=[1,2,3,4,5]
n = len(a)
result = left_rotation(a, n, k)
print(result)