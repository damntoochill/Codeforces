lucky_numbers = [4,7,44,47,74,77,444,447,474,477,744,747,774,777]
t = int(input())
def solve(t):
    for i in lucky_numbers:
        if t%i == 0:
            print("YES")
            return
    print("NO")
solve(t)  
