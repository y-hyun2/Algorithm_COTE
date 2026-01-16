N = int(input())

ans = 0
cows = [-1] * 11

for _ in range(N):
    a, b = map(int, input().split())
    if cows[a] == -1:
        cows[a] = b
    else:
        if cows[a] != b:
            ans += 1
        cows[a] = b

print(ans)