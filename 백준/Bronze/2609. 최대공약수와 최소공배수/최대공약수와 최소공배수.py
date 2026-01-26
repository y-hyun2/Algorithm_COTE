import math
a,b = map(int,input().split())

GCD = math.gcd(a,b)
LCM = math.lcm(a,b)

print(GCD)
print(LCM)