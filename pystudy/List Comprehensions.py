print(list(range(1,10)))

L = [x*x for x in range(1,11)]
print(L)

R = [x*x for x in range(1,11) if x % 2 ==0]
print(R)

H = [m+n for m in "XYZ" for n in "ABC"]
print(H)

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s,str) == True]
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')