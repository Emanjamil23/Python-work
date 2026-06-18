a=int(input("Enter your age: "))
#if statement 1
if(a%2==0):
    print("Age is even")
#end of if statement 1
#if statement 2
if(a>=18):
    print("You are above the age of consent")
    print("Good for you")
elif(a<0):
    print("you are entering invalid negative age")
elif(a==0):
    print("you are entering 0")
else:
    print("\'you are below age of consent\' ")
#end of if statement 2
print("****************End of program*****************")