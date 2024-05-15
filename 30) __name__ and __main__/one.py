def func_one():
	print("Function from Module one.py")

print("Line at level 0 of indentation from Module one.py")

if __name__ == "__main__":
	print("one.py is being run directly!")
else:
	print("one.py is imported in another module.")