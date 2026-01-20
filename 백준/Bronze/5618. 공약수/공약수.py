import math

n = int(input())
nums = list(map(int, input().split()))

if n == 2:
    g = math.gcd(nums[0], nums[1])
else:
    g = math.gcd(nums[0], math.gcd(nums[1], nums[2]))

divs = []
for i in range(1, int(g**0.5) + 1):
    if g % i == 0:
        divs.append(i)
        if i != g // i:
            divs.append(g // i)

divs.sort()
for d in divs:
    print(d)
