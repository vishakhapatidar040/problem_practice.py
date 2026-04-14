#without string math logic
num = 12321
temp = num
rev = 0
while temp > 0:
    dig = temp % 10
    rev = rev * 10 + dig
    temp = temp // 10