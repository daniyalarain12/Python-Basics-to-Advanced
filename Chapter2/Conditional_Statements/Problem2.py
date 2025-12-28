#Write a program that takes a traffic light color as input and displays the appropriate action.

color = input("ENTER TRAFFIC LIGHT COLOR : ")
if(color=="red"):
    print("STOP")
elif(color=="yellow"):
    print("LOOK") 
elif(color=="green"):
    print("GO")
else:
    print("TRAFFIC LIGHT IS BROKEN")
