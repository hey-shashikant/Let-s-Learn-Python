"""
def getInteger():
	num1 = int(input("Enter number: "))
	return num1

def Main():
	print("started")
	op = getInteger()
	print("Output is : ",op)

if __name__ == "__main__":
	Main()

"""

import keyword

print("List of keywords : ")
print(keyword.kwlist)