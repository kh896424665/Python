beforeNum = int(input())
afterNum = 0
sign = 0
if beforeNum < 0:
    beforeNum = -beforeNum
    sign = 1
while beforeNum != 0:
        a = beforeNum % 10
        beforeNum = beforeNum // 10
        afterNum = afterNum * 10 + a
if sign == 1:
    afterNum = - afterNum
if afterNum > 2**31-1 or afterNum < -2**31:
    afterNum = 0
print(afterNum)
