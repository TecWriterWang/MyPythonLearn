import threading
# 计算激活的线程
print(threading.active_count())
# 列出运行的线程
print(threading.enumerate())
# 查看当前运行的线程
print(threading.current_thread())