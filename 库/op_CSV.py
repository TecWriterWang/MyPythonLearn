import csv

with open(r'H:\PythonWorkSpace\PythonCode\File_Test\csvoperate.csv', 'r') as f:
    # 读取csv文件内容
    a_csv = csv.reader(f)
    # print(list(a_csv))
    for row in a_csv:
        print(row)

with open(r'H:\PythonWorkSpace\PythonCode\File_Test\csvoperate1.csv', 'w') as f:
    b_csv = csv.writer(f)
    b_csv.writerow(['姓名', '年龄', '薪水'])
    c = [['王5', 19, 30000], ['王5', 19, 30000], ['王5', 19, 30000]]

    b_csv.writerows(c)


