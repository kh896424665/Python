one_digit = [' zero', ' one', ' two', ' three', ' four', ' five', ' six', ' seven', ' eight', ' nine'] ##10个
two_digit =[ ' eleven', ' twelve', ' thirteen', ' fourteen', ' fifteen', ' sixteen', ' seventeen', ' eighteen', ' nineteen'] ##9个
ten_times = [' ten', ' twenty', ' thirty', ' forty', ' fifty', ' sixty', ' seventy', ' eighty', ' ninety']  ##9个
hun = " hundred"
tho = " thousand"


def oneDigit(num):
    return one_digit[num]


def twoDigit(num):
    if num %10==0:
        return ten_times[(num//10)-1]
    elif 11<=num<=19:
        return two_digit[(num%10)-1]
    else:
        return ten_times[(num//10)-1] + convert(num%10)  #取掉十位，


def threeDigit(num):
    if num %100 == 0:
        return one_digit[num//100] + hun
    else:
       return one_digit[num//100] + hun + convert(num%100)


def fourDigit(num):
    if num%1000 ==0:
        return one_digit[num // 1000] + tho
    else:
        return one_digit[num // 1000] + tho + convert(num % 1000)

def convert(num):
    if 0<=num<= 9:
        return oneDigit(num)
    elif 10<=num<=99:
        return twoDigit(num)
    elif 100<=num<=999:
        return threeDigit(num)
    elif 1000<=num<=9999:
        return fourDigit(num)
    else:
        return "请输入0—9999的数字！！！"


print("{0}  --->  {1}".format(0, convert(0)))
print("{0}  --->  {1}".format(7000, convert(7000)))
print("{0}  --->  {1}".format(1008, convert(1008)))
print("{0}  --->  {1}".format(4010, convert(4010)))
print("{0}  --->  {1}".format(1012, convert(1012)))
print("{0}  --->  {1}".format(4506, convert(4506)))
print("{0}  --->  {1}".format(9900, convert(9900)))
print("{0}  --->  {1}".format(8880, convert(8880)))
print("{0}  --->  {1}".format(5432, convert(5432)))
print("{0}  --->  {1}".format(456, convert(456)))
print("{0}  --->  {1}".format(205, convert(205)))
print("{0}  --->  {1}".format(17, convert(17)))
print("{0}  --->  {1}".format(8, convert(8)))
print("{0}  --->  {1}".format(35, convert(35)))
print("{0}  --->  {1}".format(500, convert(500)))
print("{0}  --->  {1}".format(9999, convert(9999)))
print("{0}  --->  {1}".format(123456, convert(123456)))

##写完后总结一下，这个题在写代码的时候一定要想到重复利用，不然会造成很多看似重复的代码量。就像四位数，去掉千位就是三位数，
##处理方法就和三位数一样，再去百位就是两位数，处理方法就和两位数一样。
##因此感觉这道题的优化方法还是比较多的，做起来也比较巧妙



