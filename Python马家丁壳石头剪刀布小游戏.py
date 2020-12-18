# 小项目——马家丁壳的剪刀石头布
# 作用域（要用到的变量）
name = "玩家"
hero_name = "安琪拉"
per_win = 0;  # 玩家获胜局数
com_win = 0;  # 电脑获胜局数
pk_sum = 0;  # 总的获胜局数
hero = 0;


# 1、选择英雄
# 定义一个函数来让玩家输入自己的游戏昵称以及选择对战的英雄
def selecthero():
    print("===============================欢迎来到马家丁壳对战=================================")
    global hero, name, hero_name  # 声明全局变量
    name = input("请您输入您的昵称:")
    hero = input("请您选择您的对战英雄:1、马保国 2、马云 3、马化腾")

    if hero == "1":
        hero_name = "马保国"
        print("您选择的对战英雄是 马保国")
    elif hero == "2":
        hero_name = "马云"
        print("您选择的对战英雄是 马云")
    elif hero == "3":
        hero_name = "马化腾"
        print("您选择的对战英雄是 马化腾")
    else:
        hero_name = "老龚"
        print("恭喜你触发了隐藏boss—老龚")

# 2、pk
# 通过选择1、2、3来确定选的是石头、剪刀、布，再通过石头剪刀布来确定谁获胜，当总的pk局数大于4时，即结束游戏
# 要想pk一直进行下去，就先设置一个死循环，当pk局数大于4的时候就退出循环
# pk前玩家选择123来确定石头剪刀布，电脑通过1-3的随机数来确定石头剪刀布，再通过石头剪刀布之间的关系来判断谁获胜
# 每次比赛前，比赛局数都加1，玩家获胜时，玩家获胜局数+1，电脑获胜时，电脑获胜局数+1
# 比赛局数、玩家获胜局数、电脑获胜局数都要声明时全局变量
# 要使用随机整数，就要引入随机数库


# 先定义函数来pk
def per_com_PK():
    # 声明全局变量
    global per_win, com_win, pk_sum
    print(name, "和", hero_name, "的比赛正式开始")
    # 设置死循环来实现循环PK
    while True:
        pk_sum += 1  # 每次pk开始时总局数加一

        # 玩家选择石头剪刀布
        per_key = int(input("请输入选项（1、石头，2、剪刀，3、布）："))  # input获取的是字符串，所以要将其转换成int整型
        # 显示玩家选择的结果
        if per_key == 1:
            print("您出了石头")
        elif per_key == 2:
            print("您出了剪刀")
        else:
            print("您出了布")

        # 电脑选择石头剪刀布，通过randint在1-3之间的随机数来确定
        com_key = random.randint(1, 3)
        # 显示电脑出的结果
        if com_key == 1:
            print(hero_name, "出了石头")
        elif com_key == 2:
            print(hero_name, "出了剪刀")
        else:
            print(hero_name, "出了布")

        # 下面就是pk获胜，玩家获胜的情况：石头-剪刀 or 剪刀-布 or 布-石头
        if per_key == 1 and com_key == 2 or per_key == 2 and com_key == 3 or per_key == 3 and com_key == 1:
            per_win += 1
            print(name, ":就这？")
            if hero == "1":
                print(hero_name, ":年轻人耗子尾汁")
            elif hero == "2":
                print(hero_name, ":别得意，你花呗还了吗？")
            else:
                print(hero_name, ":你的王者号没了")
        elif per_key == com_key:
            print("平局")
        else:
            com_win += 1
            print(name, ":有本事再来")
            if hero == "1":
                print(hero_name, ":年轻人你不讲武德，终究还是得败给我")
            elif hero == "2":
                print(hero_name, ":年轻人，996是福报")
            else:
                print(hero_name, ":新的王者皮肤出了哦，氪金吗")

            # 对局控制，跳出循环
        if pk_sum > 4:
            print("对局结束")
            print("欢迎再来")
            break


# 3、展示结果：总的比赛局数，玩家的获胜局数，电脑的获胜局数
def showResult():
    print("*" * 20)
    print("*" * 20)

    # 字符串格式化，来将数据和字符串结合在一起
    print("比赛共进行了%d局" % (pk_sum))
    print("%s赢了%d局" % (name, per_win))
    print("%s赢了%d局" % (hero_name, com_win))

    # 比较玩家和电话获胜局数来确定赢家
    if per_win > com_win:
        print(name, "你真棒")
    else:
        print(hero_name, ":啊？就这呀？")


# 4、结束游戏或者继续游戏
def exits():
    ex_key = input("继续游戏的话，请按“n”；退出游戏的话，请按任意键")
    if ex_key == "n":
        selecthero()
        per_com_PK()
        showResult()
    else:
        print("拜拜了您内")
        print("*" * 20)
        exit()


# 调试
import random

selecthero()
per_com_PK()
showResult()
exits()