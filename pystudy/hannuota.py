def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n - 1, a, c, b)   #先把A上的n-1个移到B
        move(1, a, b, c)       #再把A上的一个移到C
        move(n - 1, b, a, c)   #再把B上的n-1个移到C


move(3,"A","B","C")