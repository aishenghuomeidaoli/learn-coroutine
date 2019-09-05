# grep.py
#
# A very simple coroutine


def grep(pattern):
    print("Looking for %s" % pattern)
    while True:
        line = (yield)
        if pattern in line:
            print(line, end='')


# Example use
if __name__ == '__main__':
    g = grep("python")  # 创建生成器，并不执行生成器函数内代码
    # g.next()  # Python3后使用 g.send(None) 或 next(g) 方式启动生成器
    g.send(None)  # 生成器函数开始执行，并在第一个yield位置挂起，即第9行的yield

    # 向生成器传入参数，生成器函数从之前挂起的位置继续执行
    # 首先yield表达式的值为传入的参数，然后进行第9行的赋值操作，直到下一个yield处挂起
    g.send("Yeah, but no, but yeah, but no")
    g.send("A series of tubes")
    g.send("python generators rock!")
