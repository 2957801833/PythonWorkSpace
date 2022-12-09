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
        self.name=name  #家具的名字
        self.area=area  #家具的面积
    def __str__(self):
        return f"家具的名字是{self.name} 家具的面积是{self.area}"
# 2. 定义房子类
class House:
    def __init__(self,type,total_area):
        self.type=type  #房子类型： 例如 别墅、四合院、楼板房
        self.total_area=total_area  #房屋总面积
        # 新买的房子没有家具 家具列表是空的
        # 直接在初始化方法内部设置一个初始值就行
        self.item_list=[]
        # 房子剩余面积，刚买的房子剩余面积和房子面积一致
        self.free_area=total_area
    def add_item(self,hi):
        # hi 是一个形参。
        # hi 对应 就是 bed/table 对象变量
        # hi 可以理解为 是一个 家具的对象
        # ① 判断 家具的面积 是否大于 房子剩余面积
        if hi.area < self.free_area:
            # ② 如果可以存放，则添加到家具列表中
            self.item_list.append( hi.name )
            # ③ 如果可以存放，还有让剩余面积减少
            self.free_area -= hi.area
        else:
            # ④ 如果放不下就不买了
            print("买不了")
    def __str__(self):
        return f"总面积是 {self.total_area} 剩余面积 {self.free_area}" \
               f"家具列表是 {self.item_list}"
# 3. 创建家具对象
bed=HouseItem(name="席梦思",area=40)
table=HouseItem(name="桌子",area=20)
# 4. 创建房子对象
house=House(type="别墅",total_area=2000)
# 5. 房子里放家具
house.add_item(bed)
house.add_item(table)
print(house)






