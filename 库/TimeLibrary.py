import time

# time()提取当前时间获得一个浮点数，从1970年到现在，转换成秒
print(time.time())
# ctime() 提取当前时间，有标准指定格式
print(time.ctime())
# 以计算机内部格式输出时间
t = time.gmtime()
print(t)
# 时间格式化strftime(格式, 时间值)
# 年:Y 月：m数字/B英文/b英文缩写 日期：d 星期：A/a 小时：H(24)/I(12) 分钟：M 秒：S
t = time.gmtime()
print(time.strftime("%Y-%m-%d-%a %H:%M:%S", t))
# strptime(时间值， 格式) 将指定格式的时间转换成系统格式
t = "2019-08-28-Wed 13:54:49"
print(time.strptime(t, "%Y-%m-%d-%a %H:%M:%S"))

# 让程序休眠一定时间后，再继续运行
time.sleep(0.1)
# perf_counter() 计时函数返回cpu级别的精确时间计数值，单位为秒,计数值起点不固定
print(time.perf_counter())

# 文本进度条
scale = 50
print("开始计时".center(50//2, "-"))
start = time.perf_counter()
for i in range(scale+1):
    a = '*' * i
    b = '.' * (scale-i)
    c = (i/scale) * 100
    dur = time.perf_counter() - start
    print("\r{0:^3.0f}%[{1}->{2}]{3:.2f}s".format(c, a, b, dur), end='')
    time.sleep(0.1)
print("\n" + "结束计时".center(50//2, "-"))
print(len("**************************************************"))
