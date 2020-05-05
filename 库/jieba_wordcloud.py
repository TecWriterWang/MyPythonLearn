import jieba
import wordcloud
import imageio

'''
jieba.lcut(s)——精确模式切分，返回列表类型
jieba.lcut(s,cut_all=True)——全模式切分，返回列表类型
jieba.lcut_for_search(s)——搜索引擎模式切分，返回列表类型
jieba.add_word(w)——向分词词典添加新的词语
'''

file_path4 = r"H:\PythonWorkSpace\PythonCode\File_Test\Chinese.txt"
try:
    txt = open(file_path4, 'r', encoding="UTF-8").read()
    txt = txt.replace(" ", "")
    txt = txt.replace("\n", "")
except FileNotFoundError:
    print("位置不存在，请检查位置是否正确")

print(txt)
# jieba分词后返回列表
# print(jieba.lcut(txt))

# 词云可以直接处理英文单词，对中文处理时必须先使用jieba库分词
'''
w = wordcloud.WordCloud()代表一个文本对应的词云
w.generate(txt)——向w中加载文本txt
w.to_file(name)——将词云输出为.png或.jpg
三步走： 
1.配置对象参数：wordcloud.WordCloud()

默认width=200，height=400，min_font_size=4最小字号，max_font_size最大字号，

font_step=1 词云之间字体大小间隔，font_path="xxx.ttc"默认为None，max_words最大单词数量，

stopwords排除词列表，mask指定词云形状（需要配合imageio.imread（pic_path）使用），
图片边缘轮廓必须明显

background_color="white"背景颜色,默认为黑色
contour_width指定轮廓线宽度，比如contour_width=1
contour_color指定轮廓线颜色，比如contour_color='red'

2.加载词云文本，词云文本之间使用空格区分词
w.generate(txt)

3.输出词云文件,到当前工作空间
w.to_file(name)

'''
txt1 = ''''''
mk = imageio.imread('Love.png')
w = wordcloud.WordCloud(mask=mk, font_path="msyh.ttc", stopwords="{ }",
                        background_color='white', contour_width=0.5, contour_color='red')
w.generate(" ".join(jieba.lcut(txt1)))
# 提取图片的颜色
image_color = wordcloud.ImageColorGenerator(mk)
# 重新对词云着色
wc_color = w.recolor(color_func=image_color)
w.to_file("bluewn.jpg")
