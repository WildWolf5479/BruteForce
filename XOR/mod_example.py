KEY = "ABC"

for i in range(0,100):
	x = KEY[i % len(KEY)]
	print(x, end="")
