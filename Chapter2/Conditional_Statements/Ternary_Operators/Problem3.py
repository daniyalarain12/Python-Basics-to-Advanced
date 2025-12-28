#Write a Python program that takes salary as input and uses conditional indexing to calculate tax as 10% or 20% based on the salary.

sal = float(input("ENTER SALARY : "))
tax = sal*(0.1,0.2) [sal>=50000]
print("TAX :",tax)
