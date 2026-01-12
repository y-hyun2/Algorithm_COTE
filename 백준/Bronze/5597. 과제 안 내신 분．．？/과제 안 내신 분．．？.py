a = []
for _ in range(28):
    x = int(input())
    a.append(x)

for i in range(1,31):
    if i not in a:
        print(i)