import requests
from bs4 import BeautifulSoup
html = requests.get("http://www.ngchina.com.cn/animals/").text
soup = BeautifulSoup(html, features='lxml')
img_ul = soup.find_all('ul', {'class': 'img_list'})
print(len(img_ul))
# for ul in img_ul:
#     imgs = ul.find_all('img')
#
# print(r.url)



# print(r.status_code)
# print(r.headers['content-type'])
# print(r.encoding)
# file_path4 = r"H:\PythonWorkSpace\LearnPythonBaseCode\File_Test\one.txt"
# t1 = open(file_path4, "w+", encoding="utf-8")
# t1.write(r.text)

# s = requests.Session()
#
# s.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
# r = s.get('https://httpbin.org/cookies')
# print(r.text)