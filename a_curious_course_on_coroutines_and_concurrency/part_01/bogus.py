# bogus.py
#
# Bogus example of a generator that produces and receives values


def countdown(n):
    print("Counting down from ", n)
    while n >= 0:
        new_value = (yield n)
        # If a new value got sent in, reset n with it
        if new_value is not None:
            n = new_value
        else:
            n -= 1


if __name__ == '__main__':
    # The holy grail countdown
    c = countdown(5)
    for x in c:
        print(x)
        if x == 5:
            c.send(3)

# 代码输出是：
# Counting down from  5
# 5
# 2
# 1
# 0
# 现在说一下执行过程：
# 1. countdown是一个生成器函数，可以通过for循环隐式的执行生成器函数，并获取其产出的值；
# 2. 第一次遍历时，代码由第20行进入执行countdown函数，执行至第9行，n为5，
#    生成器在第9行挂起（执行yield n，未执行赋值语句）并产出5，回到第20行，x为5，
#    第21行，print(5)；
# 3. 继续执行至第23行，向生成器发送数据 3，此时生成器从之前挂起的位置(即第9行)继续执行，
#    第9行的yield 表达式的值为第23行传入的参数，即3，然后进行赋值操作，即new_value = 3，
#    继续执行第12行后，n为3，进入下一轮循环，在第9行yield 处再次挂起，产出3；
# 4. 回到进入生成器函数前的23行，c.send(3)表达式值为生成器的产出值，即3；
# 5. 回到20行继续执行下一次迭代，此时再次进入生成器，从挂起的第9行开始执行，
#    迭代进入生成器并不会向其发送任何数据，
#    所以第9行yield表达式的值为None，new_value 也为 None，
#    执行14行后，n为2，生成器函数进入下一轮循环，在第9行再次挂起，产出2；
# 6. 回到第20行，x为生成器产出的2，执行第21行 print(2);
# 7. 之后重复5、6步骤，分别打印出了1，0
