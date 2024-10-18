def leader(a,n):
  ans = []

  for i in range(n):
        leader = True
        for j in range(i+1, n):
           if a[j] > a[i] :
              leader = False
              break
      
        if leader:
           ans.append(a[i])

  return ans
n = 6
a = [10, 22, 12, 3, 0, 6]
print(leader(a, n))
