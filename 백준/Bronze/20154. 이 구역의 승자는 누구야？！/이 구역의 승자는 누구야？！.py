S = input()

a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
b = '32123333113133122212112221'
# c = list(a)
# d = list(b)

# point = dict(zip(c,d))

point = {a[i]: int(b[i]) for i in range(26)}

# e = list(S)
nums = [point[ch] for ch in S]

while len(nums) > 1:
    next_nums = []
    for i in range(0,len(nums),2):
        if i + 1 < len(nums):
            next_nums.append((nums[i]+nums[i+1]) % 10)
        else:
            next_nums.append(nums[i])
    nums = next_nums

if nums[0] % 2 == 1:
    print("I'm a winner!")
else:
    print("You're the winner?")
        