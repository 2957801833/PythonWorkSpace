# # 登录
# class LoginPage:
#     def __init__(self,usename,password,code="8888"):
#         self.usename=usename
#         self.password=password
#         self.code=code
#     # 模拟登录
#     def login(self):
#         print(f"用户名是{self.usename}")
#         print(f"密码是{self.password}")
#         print(f"验证码是{self.code}")
# # 创建对象
# # 对象变量名=类名()
# # 类名后必须跟小括号
# # 小括号的参数参照init方法参数（self不算）
# tpshop = LoginPage("13800001111","123456",)
# #调用方法
# tpshop.login()

# 食物 类
# 类名： Food
# 属性： 名字
# 方法： xxx
# 人类
# 类名： Person
# 属性： name
# 方法：eat（食物对象）
# 人 吃 食物
# class Food:
#     def __init__(self,name):
#         self.name=name
# class Person:
#     # 为区分与Food类之间的属性，定义为user
#     def __init__(self,user):
#         self.user=user
#     def eat(self,food):
#         print(f"{self.user}is eat {food.name}")
# # 创建食物对象
# egg = Food("鸡蛋")
# baozi = Food("包子")
# bread = Food("面包")
# # 创建人对象
# xiaozhang = Person("小张")
# # 调用对象
# xiaozhang.eat(egg)
# xiaozhang.eat(baozi)
# xiaozhang.eat(bread)

"""
1. 房子(House) 有 户型、总面积 和 家具名称列表
– 新房子没有任何的家具
2. 家具(HouseItem) 有 名字 和 占地面积，其中
– 席梦思(bed) 占地 4 平米
– 衣柜(chest) 占地 2 平米
– 餐桌(table) 占地 1.5 平米

家具(HouseItem)           食物
属性： name,area
方法: init,str
房子(House)               人
属性： type,total_area,item_list
方法： add_item(家具对象)
房子里放着家具             人吃食物
"""
# 1. 定义家具类
class HouseItem:
    def __init__(self,name,area):
        # 家具的名字
        self.name = name
        # 家具的面积
        self.area = area
    def __str__(self):
        return f"家居的名称是{self.name}，家具的面积{self.area}"
# 2. 定义房子类
class House:
    def __init__(self,type,total_area):
        # 房子类型： 例如 别墅、四合院、楼板房
        self.type = type
        # 房屋总面积
        self.total_area = total_area
        # 新买的房子没有家具 家具列表是空的
        # 直接在初始化方法内部设置一个初始值就行
        self.item_list = []
        # 房子剩余面积，刚买的房子剩余面积和房子面积一致
        self.free_area = total_area
    def add_item(self,hi):
        # hi是一个形参
        # hi对应bed/table 对象变量
        # hi 可以理解为是 一个 家具的对象
        # ① 判断 家具的面积 是否大于 房子剩余面积
        if hi.area < self.free_area:
            # ② 如果可以存放，则添加到家具列表中
            self.item_list.append(hi.name)
            # ③ 如果可以存放，还有让剩余面积减少
            self.free_area -= hi.area
        else:
            # ④ 如果放不下就不买了
            print("放不下不买了")
    def __str__(self):
        return f"总面积为{self.total_area}" \
               f"剩余面积为{self.free_area}" \
               f"家具列表为{self.item_list}"

# 3. 创建家具对象
bed = HouseItem(name="大木板",area=40)
table = HouseItem(name="桌子",area=20)
# 4. 创建房子对象
house = House(type="大山洞",total_area=2222)
# 5. 房子里放家具
house.add_item(bed)
house.add_item(table)
print(house)



