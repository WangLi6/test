print("hello world")
print(23)
print(34.3)
print(True)
print(())   #元组tuple
print([])   #数组list
print({})   #字典dict

'''
多行注释
'''

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

'''
通过代码获取两端内容，并且计算他们的长度和
'''
a=input("请输入：")
b=input("请输入：")
print("长度和为：",len(a+b))