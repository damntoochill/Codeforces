n = int(input())
count = 0
while(n):
    digit = n%10
    if digit == 4 or digit== 7:
        count += 1
    n = n//10
if count==4 or count== 7:
    print("YES")
else:
    print("NO")
    
