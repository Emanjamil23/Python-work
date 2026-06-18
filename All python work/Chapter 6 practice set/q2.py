marks1=int(input("Enter marks of subject 1: "))
marks2=int(input("Enter marks of subject 2: "))
marks3=int(input("Enter marks of subject 3: "))

total_percentage=(100*(marks1+marks2+marks3))/300

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("*****Congrats!!You are Pass!*****",total_percentage)
else:
    print("*****You Failed!!Try Again next year!*****",total_percentage)
