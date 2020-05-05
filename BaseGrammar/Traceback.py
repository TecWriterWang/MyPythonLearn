# 异常
import traceback

# BaseException 所有异常基类
try:
	n = int(input('Please input the division:'))
	# 测试输入是什么类型
	print(type(n))
	print(isinstance(n, int))
	answer = 5/int(n)
# 	自定义异常
	if n < 0:
		raise NameError

except ZeroDivisionError:
	print('除数为零')
except ValueError:
	with open('a.txt', 'a') as f:
		# 将异常写入到文件中
		traceback.print_exc(file=f)

	# print("zero don't as division")
	# 抛出栈错误
	# print("except:", e)
	print("Your input isn't number, please input number again!")

# 有其他操作进入
else:
	print(answer)
# 不管有没有错误都会进入
finally:
	print("error has solved")

	
def count_words(filename1):

	try:
		with open(filename1) as operate_file:
			content1 = operate_file.read()
	except FileNotFoundError:
		msg = "The " + filename1 + " don't exist!"
		print(msg)
	else:
		title = content1.split()
		# split()函数将以空格分割字符串，并将分割的元素存储在列表中
		print(
			"The first three words is", title[0:3],
			"the", filename1, "length is ", len(title))


filenames = [
	'File_Test/one.txt', 'File_Test/two.txt', 'File_Test/three3.txt', '444.txx']
for filename in filenames:
	count_words(filename)

