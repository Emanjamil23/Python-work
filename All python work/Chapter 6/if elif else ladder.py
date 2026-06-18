a=int(input("Enter your age: "))
if(a>=18):
    print("You are above the age of consent")
    print("Good for you")
elif(a<0):
    print("you are entering invalid negative age")
elif(a==0):
    print("you are entering 0")
else:
    print("\'you are below age of consent \' ")

print("****************End of program*****************")