now_time = input()
output_time = input()

# now_time = "12:34:56"
# parts = now_time.split(':')
# parts_b = ouput_time.split(':')

h, m, s = map(int, now_time.split(':'))
h2, m2, s2 = map(int, output_time.split(':'))

now_sec = h * 3600 + m*60 + s
out_sec = h2 * 3600 + m2*60 +s2

diff = out_sec - now_sec
if diff<= 0 :
    diff += 24*60*60

hh = diff// 3600
mm = (diff % 3600) // 60
# ss = ((diff% 3600) // 60 ) %60
ss = diff % 60

print(f"{hh:02d}:{mm:02d}:{ss:02d}")