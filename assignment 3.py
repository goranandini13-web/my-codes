#find max no.--question 1.
def maximum(a,b,c):
    return max(a,b,c)
print (maximum(10,20,90))

#question2---
def distinct(lst):
    return list(set(lst))
print(distinct([1,2,2,3,4,4,5]))

#question 3---

def multiply(numbers):
    result = 1
    for num in numbers:
        result = result*num
    return result

print(multiply([2,3,4,5]))

#question4----
def factorial(n):
    f = 1
    for i in range(1,n+1):
        f = f * i
    print(f)

factorial(6)

#question 5--
def reverse(s):
    print(s[::-1])
reverse("this is a programming language")

#question6---
def check(n):
    if 1<=n <=10:
        print("in range")
    else:
        print("not in range")
check(9)

#question7---
def even(lst):
     for i in lst:
         if i % 2 == 0:
             print(i)
even([1,2,3,4,5,6])          

#question8---
def prime(n):
    if n > 1:
        for i in range(2,n):
            if n % i == 0:
                print ("not prime")
                return
            print("prime")
        else:
            print("not prime")
prime(4)            

#quetion9----
def count(s):
    upper = 0
    lower = 0

    for i in s:
        if i.isupper():
            upper += 1
        elif i.islower():
          lower += 1
    print("upper =",upper)
    print("lower =",lower)  

count("hello world")    

#question10------

#write file
f = open("file.txt","w")
f.write("hello")
f.close()

#read file
f=open("file.txt","r")
print(f.read())
f.close()

#append file
f=open("file.txt","a")
f.write("world")
f.close()
    
