password = 'a123456'
count = 0
while count < 3:
    User = input("請輸入密碼:")
    if User == password:
        print("登入成功")
        break
    else:
        print("密碼錯誤!還有", 2-count, "次機會")
        count = count + 1
print("此帳號已被封鎖")
