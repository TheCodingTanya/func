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

wash(water=10)
# wash() # 使用function

def say_hi():
	print('hi')

# say_hi()


def add(x, y):
	return x + y # 回傳result中的3投進x, 4投進y, result =7

result = add(3, 4)
print(result)


def average(numbers):
	return sum(numbers) / len(numbers)
	

a = average([1, 2, 3])
print(a)