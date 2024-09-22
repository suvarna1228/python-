def move_end(a):
 temp=[num for num in a if num != 0]
 temp2= len(a)-len(temp)
 return temp+[0]*temp2
a=[34,0,54,67,89 ,0,2,45,]
result = move_end(a)
print(result) 

