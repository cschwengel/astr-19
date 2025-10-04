#Connor Schwengel
#10/4/25

def sum():
	print("Sum of floats")
	a=input("Enter a number: ")
	a=float(a)
	b=input("Enter a number: ")
	b=float(b)
	c=a+b
	print(c)
	print(type(c))

def difference():
	print("Difference of integers")
	d=input("Enter an integer: ")
	d=int(d)
	e=input("Enter an integer: ")
	e=int(e)
	f=d-e
	print(f)
	print(type(f))

def product():
	print("Product of an integer and a float")
	g=input("Enter a number: ")
	g=float(g)
	h=input("Enter an integer: ")
	h=int(h)
	j=g*h
	print(j)
	print(type(j))

def main():
	sum()
	difference()
	product()

if __name__ == '__main__':
	main()