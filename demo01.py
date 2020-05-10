'''
print("hello world")
print(23)
print(34.3)
print(True)
print(())   #元组tuple
print([])   #数组list
print({})   #字典dict

#多行注释

print("hello",23234,342)
print("hello"+"world")  #字符串拼接
print("hello"*10)
print(3>2)

name="哈哈哈"
print(name)

a=input("请输入：")
print("输入的内容为："+a)
print(len(a))

#数据格式的转换
print(type(a))

a=float(input("请输入："))
b=float(input("请输入："))
print("a+b=",a+b)

#通过代码获取两端内容，并且计算他们的长度和
a=input("请输入：")
b=input("请输入：")
print("长度和为：",len(a+b))

print("我好像明白了，哈哈哈哈，好开心啊")
print("ok")
print("完美！！！")
'''

# 元组，下标，从0开始编号
# a=(1,3,3.4,4.5,"很好","嘻嘻","哈哈","哈哈","哈哈",True,False)
# print(a)
# 切片
# print(a[:5])    #左闭右开
# print(a[5:7])
# print(a[7:])

# print(a.index("哈哈"))
# print(a.count("哈哈"))

# 二维数组
# b=(a,"hh","xx")
# print(b[0][2])

# 元组写好后不可以修改，而数组是可以修改的
'''
a=[3,4,5,6,"哈哈","嘻嘻","哇哇","凄凄",True,False]
# 添加到数组最后面
a.append("append1")
print(a)
# 插入到指定下标中
a.insert(3,"insert1")
print(a)
# 剪切
b=a.pop(0)
c=a.pop(0)
print(a)
print(b)
print(b+c)
# 清除
a.clear()
print(a)
xx=["你好","你好呀"]
a.extend(xx)
print(a)
#print(a+xx)
# 移除
a.remove("你好")
print(a)
# 下标不要超出范围=越界
'''
'''
python的语法：
    所有的方法都是小括号结尾。比如，print(),input(),len()....
    元组、数组、字典的取值，都是用中括号，比如b[0]
    元组、数组、字典的定义，分别是(),[],{}
'''

'''
字典的特点：
    字典中的值没有顺序
    字典的结构必须是键值对的形式。 key:value
'''
a={"name":"wang","age":20,"id":13}
print(a)
# 取值 (如果是不存在的值,get()显示None,直接获取会报错)
print(a["name"])
print(a.get("name"))
# 新增
a["high"]="160cm"
print(a)
# 修改
a["name"]="li"
print(a)
a.update(name="哈哈")
print(a)
# 剪切
b=a.pop("name")
print(b)
print(a)

# 数组和字典的删除
del a['high']
print(a)

a=[2,3,4]
del a[0]
print(a)

'''
获取用户输入的个人信息，并且存储到字典中
个人信息：name，age，sex
'''
b=input("请输入name：")
c=input("请输入age：")
d=input("请输入sex：")
a={"name":b,"age":c,"sex":d}
print(a)