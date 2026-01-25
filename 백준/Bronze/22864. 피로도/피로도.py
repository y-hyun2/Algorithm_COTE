A,B,C,M =map(int,input().split())

# 피로도
T = 0
# 작업량
DW = 0

for _ in range(24):
    if T > M:
        print(0)
    else: 
        if T + A <= M:
            T += A
            DW += B
        else:
            if T-C >= 0:
                T -= C
            else:
                T = 0
print(DW)