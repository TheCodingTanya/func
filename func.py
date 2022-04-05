# function 函式/功能

# function是用來[收納]程式碼的
# 它是個功能不執行
dry = True

def wash(dry=False, water=8): # def是define, dry是參數
    print('加水', water, '分滿')
    print('加洗衣精')
    print('旋轉')
    if dry:
        print('烘衣')

wash()
# wash() # 使用function

def say_hi():
	print('hi')

# say_hi()


def add(x=1, y=1):
	print(x + y)

add(y=5)