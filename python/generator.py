def test():
	print("A")
	yield 1
	print("B")
	yield 2
	print("C")

output = test()
a = next(output)
test()
print(a)
b = next(output)
print(b)
