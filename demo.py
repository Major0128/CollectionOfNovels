import os
import re

myfile = open('E:\\Book\\DaYing\\txt\\大隐.txt', 'a')
# 遍历目录下的所有txt文件
for fileName in os.listdir(r'E:\Book\DaYing\txt'):
    filePath = "E:\\Book\\DaYing\\txt\\" + fileName
    # print(filePath)
    # filePath = "E:\\Book\\DaYing\\txt\\01_3.txt"
    # 打开文件
    file = open(filePath, 'r')
    fileContent = file.read()
    file.close()
    # 替换\u3000空字符
    fileContent = fileContent.replace("\u3000", "")
    # 获取标题
    tittle = re.search('(?<=\'\>)[^\<\/]+', fileContent, flags=0).group()
    myfile.write(tittle+"\n")
    # print(tittle)
    # 获取文本内容
    pattern = re.compile(r'(?<=\<p\>)[^\<p\>]+')
    content = pattern.findall(fileContent)
    # 第一个进行特殊处理
    patternP1 = re.compile(r'')
    contentP1 = content[0].split('\'')[1]
    content[0] = contentP1
    # print(content[0:len(content) - 1])
    # 遍历列表写入文件，最后一个不需要
    for contentText in content[0:len(content) - 1]:
        myfile.write("  "+contentText+"\n")
myfile.close()

