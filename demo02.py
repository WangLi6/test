# 判断 缩进
# age=int(input("请输入你的年龄："))
# if age<=20:
#     print("你要好好学习啊！")
# elif age>20 and age<=30:
#     print("你还年轻，你得拼搏！")
# elif age>30 and age<40:
#     print("你正直壮年，你可以的!")
# else:
#     print("你老了，该休息了！")

# a='你好'
# if a in '你好啊，春天':
#     print('OK')
# else:
#     print('NO')

# age=input("请输入年龄：")
# if age=="":
#     print("不能为空！")
#     exit()
# if age in "0123456789":
#     age = int(age)
# else:
#     print("你输入的年龄不正确！！！")
#     exit()
# if age>10:
#     print("a>10")
# else:
#     print("a<10")

# a="hhhh"
# if type(a) is int:
#     print("int")
# elif type(a) is float:
#     print("float")
# elif type(a) is str:
#     print("str")
# else:
#     print("其他")

# 循环
# a=1
# while a<3:
#     print("哈哈哈",a)
#     a+=1

'''
现在又10个学生的成绩，需要录入到系统中。
名字和成绩需要对应
大于60的和小于60的需要分开存放
'''
studentList=['张三','李四','哇哇','赵六','王五']
highScore={}
lowScore={}
a=0
while a<len(studentList):
    score=int(input("请输入"+studentList[a]+"的成绩："))
    if score>=60:
        highScore[studentList[a]]=score
    else:
        lowScore[studentList[a]]=score
    a+=1
print(highScore,lowScore)