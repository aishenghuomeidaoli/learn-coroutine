# Part 1 : Introduction to Generators and Coroutines

* [countdown.py](./countdown.py). 一个简单的生成器函数
* [follow.py](./follow.py). 一个捕捉实时写入日志文件每一行的生成器，类似于`Unix`中的`tail -f`。想要运行这个程序，需要一个日志文件搭配使用。
运行[logsim.py](./logsim.py)程序来模拟生成一个web服务器日志（向`access-log`文件写入）。接下来的部分需要保持该程序一直运行。
* [pipeline.py](./pipeline.py). 一个使用生成器建立简单管道处理的示例。打印所有包含“python”单词的服务器日志条目。
* [grep.py](./grep.py). 第一个协程函数示例。该函数接收日志条目，并且打印出包含特定子字符串的行。
* [coroutine.py](./coroutine.py). 一个在协程启动时避免执行`send(None)`的装饰器函数。
* [grepclose.py](./grepclose.py). 一个协程捕捉`close()`操作的示例。
* [bogus.py](./bogus.py). An example of a bogus generator that generates and receives values (not a recommended coding style).