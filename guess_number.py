import random
ans = random.randint(1, 100)
count = 0
while count < 3:
    num = input("請輸入 1~100 數字:")
    if int(num) == ans:
        print("恭喜你猜對了!")
        break
    else:
        print("很可惜剩下", 2-count, "次機會")
        count += 1
        if count < 3:
            if int(num) > ans:
                print("在小一點")
            else:
                print("再大一點")
print("遊戲結束答案是:", ans)
