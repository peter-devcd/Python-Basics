n=int(input("enter a number:"))

if n<0:
	print("Factorial can't be calculated for negative numbers.")
elif n == 0:
	print("Factorial is 1.")
else:
    fact=1;
	for i in range(1,n+1):
		fact=fact*i

	print("factorial is:",fact)
