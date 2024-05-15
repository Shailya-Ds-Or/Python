import one

print("Line at level 0 of indentation from Module two.py")

one.func_one()

if __name__ == "__main__":
	print("two.py is being run directly!")
else:
	print("two.py is imported in another module.")