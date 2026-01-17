N= int(input())

list = list(map(int,input().split()))

ans = 0

#소수 식별 함수
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,int(n**0.5) +1 ):
        if n % i == 0 :
            return False
    return True

for num in list:
    if is_prime(num):
        ans += 1
print(ans)