def hello(x, y=1):
	print(x + y)

hello(3, 4)

def crazy(x, y=3, z=2):
	return x * 2 + y * 3 + z

print(crazy(2))
print(crazy(3, 1))
print(crazy(3, 2, 0))


def can_vote(age):
	if age >= 18:
		return True
	else:
		return False

a = can_vote(20)
print(a)

def check_mood(color='紅'):
	mood = '好心情'
	if color == '藍':
		mood = '心情不好'
	return mood 

print(check_mood())
print(check_mood('藍'))