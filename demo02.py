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

studentList=['张三','李四','哇哇','赵六','王五']
highScore={}
lowScore={}
# a=0
# while a<len(studentList):
#     score=int(input("请输入"+studentList[a]+"的成绩："))
#     if score>=60:
#         highScore[studentList[a]]=score
#     else:
#         lowScore[studentList[a]]=score
#     a+=1
# print(highScore,lowScore)
for i in studentList:
    score=int(input("请输入"+i+"的成绩："))
    if score>=60:
        highScore[i]=score
    else:
        lowScore[i]=score
print(highScore,lowScore)
'''

# a=['hello world!!!']
# for i in a:
#     print(i)

# for i in range(0,100,2):
#     print(i)

# 打印九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(i,"*",j,"=",i*j,end="  ") # 不换行,变成空格
#     print()

'''
通过print打印，模拟一个红绿灯功能，红灯30次，绿灯35次，黄灯3次

使用代码实现一个注册功能。用户输入账号密码，要求账号长度是5-8位，密码6-12位，账号必须是小写字母开头
储存到字典中{username:password}
'''
# while True:
#     for i in range(30,-1,-1):
#         print("红灯还剩",i,"s")
#     for i in range(35,-1,-1):
#         print("绿灯还剩",i,"s")
#     for i in range(3,-1,-1):
#         print("黄灯还剩",i,"s")

# light={"红灯":30,"绿灯":35,"黄灯":3}
# while True:
#     for i in light:
#         for j in range(light[i]):
#             print(i,"倒计时还有",light[i]-j,"s")

# user=input("请输入注册账号：")
# pwd=input("请输入密码：")
# if len(user)>=5 and len(user)<=8:
#     if len(pwd)>=6 and len(pwd)<=12:
#         if user[0]>='a' and user[0]<='z':
#             print("注册成功！！！",user,pwd)
#         else:
#             print("账号第一位不是小写字母！！！")
#     else:
#         print("密码长度错误！！！")
# else:
#     print("账号长度错误！！！")


# continue,break
# for i in range(5):
#     if i==3:
#         break
#     print(i)

# 方法
# def checkName(username):
#     '''
#     用户输入账号,账号长度是5-8位，账号必须是小写字母开头
#     '''
#     if len(username)>=5 and len(username)<=8:
#         if username[0]>='a' and username[0]<='z':
#             print("OK")
#         else:
#                 print("账号第一位不是小写字母！！！")
#     else:
#         print("账号长度错误！！！")
# checkName("hhhhh")
# '''方法的说明'''
'''
def 方法的声明
checkName 方法的名字
username 方法的参数
方法的逻辑代码
'''

# def add(a,b):
#     if type(a) is int and type(b) is int: 
#         print(a+b)
#     else:
#         print("输入的数据类型不正确！！！")
# add(4,5)

# def add(a,b):
#     if type(a) is int and type(b) is int: 
#         return a+b
#     else:
#         print("输入的数据类型不正确！！！")
# '''
# 返回值，返回后我们可以对这个值做其他操作，而print不能
# '''
# print(add(4,5))


# 异常捕获
# try:
#     print("a"+1)
# except:
#     print("上面的代码写错了！！！")

# 包--类--方法--变量（并列）
# 异常类
# try:
#     print('a'+1)
# except Exception as e:
#     print(e)

# 处理用户输入的数据
# a=input("请输入你的年龄：")
# try:
#     if int(a)>18:
#         print(a,"成年了")
#     else:
#         print(a,"未成年")
# except Exception as e:
#     print("请输入正确的年龄",e)