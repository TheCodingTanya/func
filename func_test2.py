def is_leap(year):
	if year % 4 != 0:
		return False
	elif year % 100 != 0:
		return True
	elif year % 400 != 0:
		return False
	elif year % 3200 != 0:
		return True
	else:
		return False

print(is_leap(2022))
print(is_leap(1985))
print(is_leap(2020))
print(is_leap(2021))
print(is_leap(1993))
print(is_leap(1632))