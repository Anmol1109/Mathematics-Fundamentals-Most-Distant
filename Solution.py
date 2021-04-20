from math import sqrt
n = int(input())
min_x,max_x,min_y,max_y = 0,0,0,0
for i in range(n):
    x,y = tuple(map(float,input().split()))
    if x < min_x:
        min_x = x
    if x > max_x:
        max_x = x
    if y < min_y:
        min_y = y
    if y > max_y:
        max_y = y
        
opts = min_x,max_x,min_y,max_y
res = max([max_x - min_x,max_y - min_y,sqrt(max_x**2 + max_y**2),sqrt(max_x**2 + min_y**2),sqrt(min_x**2 + max_y**2),sqrt(min_x**2 + min_y**2)])
print(res)