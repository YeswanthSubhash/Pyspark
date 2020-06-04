import sys

#File read

#List
l=[1,2,3,4,5,6]
print(type(l))
print(l[2])
print(l[:3])
print(l[2:5]) #l[position at 2:length 5]

#set
s={1,2,3,4,5,6,1,2,3}
print(type(s))
#print(s[0])  @ Set doesnot have Index so it will trow error
print(s) #set have only unique values
print(len(s))

#dictionary
d={1:"Hello",2:"World",3:"How are You"}
print(d)
print(d[1])


l=[1,2,3,4,5,6,6,1,2,4]
print(l.count(1))
print(l.count(6)) #count -> No of times the element is repeated
print(l.index(6,3,9)) #index(element to be searched,start ,stop index)
l.insert(0,10) #insert value 10 to its 0th position
print(l)
print(l.pop(10)) # 10 is the index and return the deleted value
print(l.remove(6)) # removed 6 and return the None
l2 = l.reverse() # reverse the order of elements in the List l
print(l2)
print(l)
l3=l.sort() #sort the elements in the list l
print(l)

s={1,2,3,4,5,6,6,1,2,4}

print(type(s))
print(s) #Eliminate the duplicates
print(1 in s) # IN operatior
#intersection
s1={1,2,3,10,20,30}
print(s.intersection(s1)) #intersection
print(s.difference(s1)) #difference
print(s.union(s1)) #union
s_sort=list(s).sort(reverse=True)
print(s)

d={1:'Hello',2:'World',3:'Python'}
print(d)
d[1]="How are you" #update
print(d)
d2={1:"Hai",3:"Scala"}
d.update(d2) #update from other dict
print(d)
print(d.keys()) #keys
print(d.values())#values
print(d.items())


def readData(filePath):
    tagFile=open(filePath)
    tagData=tagFile.read()
    tagDatacoll=tagData.splitlines()
    return  tagDatacoll

tags=readData("D:\\spark performance\\question_tags.csv")
questions=readData("D:\\spark performance\\questions.csv")
print(tags[:10])
print(questions[:10])

tags.sort(key=lambda k:(k.split(",")[1]),reverse=True)
print(tags[:10])
tag1=sorted(tags,key=lambda k:(k.split(",")[1])[:10],reverse=True)
print(tag1)

'''-------Task-----'''
s=set({})
for i in tag1[:10]:
    s.add(i.split(',')[1])

print(s)


'''----Task End----'''











