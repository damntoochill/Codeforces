n = int(input())
while(True):
    n = n+1
    a = n%10
    b = (n//10)%10
    c = (n//100)%10
    d = (n//1000)
    if(a != b and a != c and a != d and b != c and b != d and c != d):
        break
print(n)
