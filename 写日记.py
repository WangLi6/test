# 文件的读写
import time
now=time.strftime("%y-%m-%d %H:%M:%S")
text=input("请输入今天的心情：")
# w是写入，a是追加
with open("日记.txt","a",encoding="utf8") as f:
# with open("D:\日记.txt","a",encoding="utf8") as f:
    f.write(now+"\n")
    f.write(text+"\n")
    f.write("--------------------------\n")