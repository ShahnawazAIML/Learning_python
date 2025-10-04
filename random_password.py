import random

strings = "abcdefghijklmnopqrstuvwxyz"
capital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
special = "@#$&*?!/."

userlimit = int(input("How big password you want? "))
password = ""

for i in range(1, userlimit + 1):
	a = random.randint(1,4)
	if a == 1:
		x = random.randint(0,25)
		gen = strings[x]
		password = password + gen
	elif a == 2:
		x = random.randint(0,25)
		gen = capital[x]
		password = password + gen
	elif a == 3:
		x = random.randint(0,9)
		gen = number[x]
		password = password + gen
	else:
		x = random.randint(0, 8)
		gen = special[x]
		password = password + gen
		
print(password)