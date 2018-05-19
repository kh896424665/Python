def triangles():
    result = [1]
    while True:
        yield result    # 包含yield的函数是一个生成器generator，运行到此处停止
        result = [1]+[result[x] + result[x+1] for x in range(len(result)-1)]+[1]   #此处用列表生成器

def draw_triangles(n):
    for item in triangles():
        print(item)
        n = n-1
        if n == 0:
            break

draw_triangles(50)
