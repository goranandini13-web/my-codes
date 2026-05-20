#dictionary---question1
student={"name":"Nandini",
         "age":21,
         "course":"Btech"}
print(student)
print(student["name"])

#dict
d={1:'python',2:'java',3:'c++'}
print(d)

#tuple---
n=(10,20,203,40,50,40)
print(n)
print(n[1])

#set--
books={"math","python","english","geography","english"}
print(books)


#question2-----
num1=int(input("enter a 1 number"))
num2=int(input("enter a  2 number"))
print("addition=",num1+num2)
print("subtraction=",num1-num2)
print("multiply=",num1*num2)
print("division=",num1+num2)

#question3-----
num=input("enter a number:")
if num==num[::-1]:
    print("palindrome number:")
else:
    print("not palindrome")

