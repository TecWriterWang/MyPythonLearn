
# 集合set = {}
# Python中的集合跟数学上的集合是一致的，不允许有重复元素，而且可以进行交集、并集、差集等运算。

a = {'1', '2', '3'}
b = {'2', '3', '6'}
# 集合a和b并集
print(a | b)
# 两个集合相减
print(a - b)
# 两个集合交集
print(a & b)
# 输出两个集合中互相不存在的元素 补运算
print(a ^ b)


set1 = {1, 2, 3, 3, 3, 2}
print(set1)
set2 = set(range(1, 10))
print(set2)
# 元祖转化为集合
set3 = set((1, 2, 3, 3, 2, 1))
print(set3)
# 集合增加元素
set1.add(4)
print(set1)
# 集合中增加列表
set2.update([11, 12])
print(set2)
# 移除集合所有元素clear()
print(set1.clear())
# 移除集合中指定元素remove（）、discard（）
# remove() 移除的元素不存在会报错
set2.remove(11)
print(set2)
# discard() 移除的元素不存在不会报错
set2.discard(14)
print(set2)
# pop() 从集合中随机弹出一个元素,弹出的元素可以使用，集合中将删除该弹出的元素
print(set3.pop())
print(set3)
# 复制集合,返回集合副本
set2.copy()
# set()将其它类型数据转换为集合
print(set("111234"))
number = input()

nums = set()
while number != "":
    nums.add(eval(number))
    number = input()
nums = list(nums)
sum = 0
for item in nums:
    sum += item
print(sum)


s = '''双儿 洪七公 赵敏 赵敏 逍遥子 鳌拜 殷天正 金轮法王 乔峰 杨过 洪七公 郭靖 
       杨逍 鳌拜 殷天正 段誉 杨逍 慕容复 阿紫 慕容复 郭芙 乔峰 令狐冲 郭芙 
       金轮法王 小龙女 杨过 慕容复 梅超风 李莫愁 洪七公 张无忌 梅超风 杨逍 
       鳌拜 岳不群 黄药师 黄蓉 段誉 金轮法王 忽必烈 忽必烈 张三丰 乔峰 乔峰 
       阿紫 乔峰 金轮法王 袁冠南 张无忌 郭襄 黄蓉 李莫愁 赵敏 赵敏 郭芙 张三丰 
       乔峰 赵敏 梅超风 双儿 鳌拜 陈家洛 袁冠南 郭芙 郭芙 杨逍 赵敏 金轮法王 
       忽必烈 慕容复 张三丰 赵敏 杨逍 令狐冲 黄药师 袁冠南 杨逍 完颜洪烈 殷天正 
       李莫愁 阿紫 逍遥子 乔峰 逍遥子 完颜洪烈 郭芙 杨逍 张无忌 杨过 慕容复 
       逍遥子 虚竹 双儿 乔峰 郭芙 黄蓉 李莫愁 陈家洛 杨过 忽必烈 鳌拜 王语嫣 
       洪七公 韦小宝 阿朱 梅超风 段誉 岳灵珊 完颜洪烈 乔峰 段誉 杨过 杨过 慕容复 
       黄蓉 杨过 阿紫 杨逍 张三丰 张三丰 赵敏 张三丰 杨逍 黄蓉 金轮法王 郭襄 
       张三丰 令狐冲 赵敏 郭芙 韦小宝 黄药师 阿紫 韦小宝 金轮法王 杨逍 令狐冲 阿紫 
       洪七公 袁冠南 双儿 郭靖 鳌拜 谢逊 阿紫 郭襄 梅超风 张无忌 段誉 忽必烈 
       完颜洪烈 双儿 逍遥子 谢逊 完颜洪烈 殷天正 金轮法王 张三丰 双儿 郭襄 阿朱 
       郭襄 双儿 李莫愁 郭襄 忽必烈 金轮法王 张无忌 鳌拜 忽必烈 郭襄 令狐冲 
       谢逊 梅超风 殷天正 段誉 袁冠南 张三丰 王语嫣 阿紫 谢逊 杨过 郭靖 黄蓉 
       双儿 灭绝师太 段誉 张无忌 陈家洛 黄蓉 鳌拜 黄药师 逍遥子 忽必烈 赵敏 
       逍遥子 完颜洪烈 金轮法王 双儿 鳌拜 洪七公 郭芙 郭襄 赵敏'''
word = {}
words = s.split()
for item in words:
    word[item] = word.get(item, 0) + 1
word = list(word.items())
# key指定以列表中某个参数来排序
word.sort(key=lambda x: x[1], reverse=True)
name, count = word[0]
print(word)
print(name)
key = lambda x: x[1]
print(key("121"))


