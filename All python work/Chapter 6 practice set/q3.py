p1='Make a lot of money'
p2='buy now'
p3='subscribe this'
p4='click this'
message=input("Your comment : ")
if((p1 in message) and (p2 in message) and (p3 in message) and (p4 in message)):
    print("This is a Spam")
else:
    print("Not a spam")

