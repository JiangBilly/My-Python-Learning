import random
secret = random.randint(1,10)
print(".....Billy Studio......")
temp = input("不妨猜一下我心里想的数字：")
guess = int(temp)
while guess != secret:
    temp = input("猜错了，请重猜：")
    guess = int(temp)
    if guess == secret:
        print("答对了，你是我心里的蛔虫吗？")
        print("猜中了也没有奖励！")
    else:
        if guess > secret:
            print("大了")
        else:
            print("小了")
print("game over!")
