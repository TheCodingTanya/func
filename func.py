# function 函式/功能

# function是用來[收納]程式碼的
# 它是個功能不執行

def wash(dry): # def是define, dry是參數
	print('加水')
	print('加洗衣精')
	print('旋轉')
	if dry:
		print('烘衣')

wash(True) # 使用functionR, True投進dry, 印出烘衣
wash(False) #第二次將False投進, 就沒烘衣

def say_hi():
	print('hi')

# say_hi()


def add(x, y):
	print(x + y)

add(3, 4)  # 3投入x, 4投入y
add(123, 2323) # 123投入x, 2323投入y