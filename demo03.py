import time # 导包
import random
import pymysql

# for i in range(4):
#     time.sleep(1)
#     print(i)
# a=random.randint(1,100)
# print(a) # 1-100的随机数


# db=pymysql.connect(host="127.0.0.1",user="root",password="123456",db="testdb")
# cur=db.cursor()
# try:
#     cur.execute("select * from t_class")
#     res=cur.fetchall()
#     print(res)
# except:
#     print("sql语句错误！")


'''
class 声明类的名字
类的名字必须大写
面向对象编程
类里面所有的方法，都必须要传一个参数，self
'''
class GirlFriend():
    '''
    哈哈哈
    '''
    def __init__(self,sex,high,weight,hair,age):
        self.sex=sex
        self.high=high
        self.weight=weight
        self.hair=hair
        self.age=age
    def caiyi(self,num):
        '''
        才艺表演
        '''
        print("你的性别为"+self.sex+"身高"+self.high+"体重"+self.weight+"头发"+self.hair+"年龄"+self.age+"开始了自己的才艺表演之：")
        if num==1:
            print("胸口碎大石")
        elif num==2:
            print("唱跳RAP篮球")
        else:
            print("单手开瓶盖")
    def chuyi(self):
        '''
        厨艺
        '''
        print("你的性别为"+self.sex+"身高"+self.high+"体重"+self.weight+"头发"+self.hair+"年龄"+self.age+"开始了自己的厨艺表演之：")
        print("精通八大菜系，中外融合！！！")
    def work(self):
        '''
        工作
        '''
        print("你的性别为"+self.sex+"身高"+self.high+"体重"+self.weight+"头发"+self.hair+"年龄"+self.age+"开始了自己的工作之：")
        print("开挖掘机......")
# # 类的实例化
# g=GirlFriend("男","188cm","80KG","寸头","20岁")
# g.work()
# g.caiyi(2)
# print(g.hair)

# GirlFriend父类,Nvpengy子类
class Nvpengy(GirlFriend):
    def work(self):
        print("修电脑......")
zhangsan=Nvpengy("女","165cm","50KG","长发","20岁")
zhangsan.work()


# class Car():
#     def __init__(self,pinpai,yanse,neishi,jilun):
#         self.pinpai=pinpai
#         self.yanse=yanse
#         self.neishi=neishi
#         self.jilun=jilun
    
#     def bianxing(self):
#         print("车子变身......")
    
#     def fly(self):
#         print("车子起飞......")

# zhangsan=Car("奥拓","白色","豪华","独轮车")
# zhangsan.bianxing()