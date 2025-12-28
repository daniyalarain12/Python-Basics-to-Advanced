# Write a Python program that takes a food name as input and uses conditional expressions (ternary operator) to decide whether to eat it and whether the food is sweet.

food = input("INPUT FOOD : ")
eat = "yes" if food == "Cake" else "no"
print(eat)

print("sweet") if food == "Cake" or food == "Jalebi" else print("not sweet")
