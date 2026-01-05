# WRITE A FUNCTION TO PRINT THE ELEMENTS OF A LIST IN A SINGLE LINE.

def print_list(list):
    for i in list:
        print(i,end=" ")

cities = ["LAHORE","HYDERABAD","KARACHI","ISLAMABAD","QUETTA","PESHAWAR"]
print_list(cities)
