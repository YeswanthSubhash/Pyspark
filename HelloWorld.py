import sys
print("Hello world")

#Help
i=0
print(type(i))
help(int)

#Function
def checkEven():
    i=7
    if(i % 2 == 0):
        print(str(i)+" is an Even number")
    else:
        print(str(i)+"is an Odd number")

#Function Calling
checkEven()

print("""This is a paragraph.
    which is in multiline""")

a=b=c=d=10

print(a)
print(type(b))

p,q,r=10,2.5,"John"
print(p,q,"John")


#Collections
#list
l=[1,2,3,4]
#set
s={1,2,3,4}
#dict
d={"key1":"value1","key2":"value2","key3":"value3"}
#tuple
t=(1,2)

print(type(l))
print(type(s))
print(type(d))
print(type(t))

#i=3 check i is exist in list l

i=3
print(i in l)

#if...else conditions

var =10
var1=0

if var:
    print("Value is non zero")

if var1:
    print("Value is non zero")
else:
    print("Value is  zero")

var3=30

#if.....else conditions
if (var3 > 50):
    print("var is greter than 50")
elif (var3 >= 30 and var3 <=39):
    print("var3 between 30 and 40")
elif (var3 >= 20 and var3 <=29):
    print("var3 between 20 and 29")

#Loop While
counter=0
while True:
    print(counter)
    counter+=1
    if(counter>5):
        break
#Loop for
for i in range(0,10):
    if(i % 2 == 0):
        print(str(i)+" is even")
    else:
        print(str(i)+ " is odd")

#Ternary Operator
for i in range(0,10):
    print(str(i) + " is Even") if(i % 2== 0) else print(str(i)+" is Odd")

#Exception Handling
while True:
    try:
        x = int(input("Please Enter the Number: "))
        i = int(x)
        break
    except ValueError:
        print("Oops,Its not a valid Number.Please Try again")
    except(RuntimeError, TypeError, NameError):
        pass
    finally:
        print("You have typed the " + str(x))

