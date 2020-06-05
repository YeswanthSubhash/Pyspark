s='1,2019-07-11 00:00:00.0,11598,CLOSED'
s1=s.split(',')[0]
print(type(s1))
s2=int(s1)
print(type(s2))
s3=float(s1)
print(s3)
print(type(s3))
s4=1
print(type(s4))
s5=str(s4)
print(type(s5))

#to Lower and Upper
s6=s.split(',')[3].lower()
print(s6)
print(s6.upper())
print(s6.capitalize())
s7='cLOseD'
print(s7.swapcase())

#Trimming
s8="       Hello        "
print(s8)
print(s8.rstrip())
print(s8.lstrip())

#padding
s9='7'

print(s9.rjust(5,'0'))
print(s9.ljust(5,'0'))

year=2019
month=7
date=2

print( "-".join([str(year), str(month).rjust(2, "0"), str(date).rjust(2, "0")]))

#is Operator
s10='CLOSED'
print(s10.islower())
print(s10.isalnum())


'''**********************************************************'''
def printMax(x,y):
    '''Printing the maximum of two numbers...\n both the numbers  should be integers'''
    if(x>y):
        print(x,"is Greater than",y)
    else:
        print(y," is Greater than",x)

printMax(2,3)
print(printMax.__doc__)
print(printMax(2,3))
'''************************************************************'''

#multiple returns
def min_max(numbers):
    smallest=largest=numbers[0]
    for i in numbers:
        if(i>largest):
            largest=i
        elif(i<smallest):
            smallest=i
    return smallest,largest

smallest,largest=min_max([2,3,1,5,4,9,3])
print(smallest)
print(largest)
'''************************************************************'''
#override arguments

def say(s,times=1):
    print(s* times)

say("Hello")
say("Hai",8)
'''************************************************************'''
#keyword Arguments

def func(a,b=5,c=10):
    print('a=',a,' b=',b,'c=',c)

func(2)
func(2,4)
func(2,4,6)
'''************************************************************'''
#variable length arguments

def total(initial=5,*numbers):
    count=initial
    for num in numbers:
        count+=num
    return count

print(total(10,2,3,4,5))

'''************************************************************'''
#is keywords arguments

def total1(initial=5,*numbers,**keywords):
    count=initial
    for i in numbers:
        count+=i
    for k in keywords:
        count+=keywords[k]

    return count

print(total1(10,1,2,3,apple=10,mango=20,grapes=30))
'''************************************************************'''

'''lambda functions'''

print("Lambda functions")

def sum(lb,ub,f):
    total=0
    for i in range(lb,ub+1):
        print(f(i))
        total+=f(i)

    return total

print(sum(1,10,lambda x:x))
print(sum(1,10,lambda x:x+1))
print(sum(1,10,lambda x:x*2))

def getEven(x):
    if(x%2==0):
        return x
    else:
        return 0

print(sum(1,10,lambda x:getEven(x)))
