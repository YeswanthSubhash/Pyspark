
def readData(filePath):
    readFile=open(filePath)
    dataStr=readFile.read()
    dataList=dataStr.splitlines()
    return dataList

dataList=readData("D:\\spark performance\\question_tags.csv")
#print(dataList)

s=set({})
for i in dataList[:10]:
   s.add(i.split(',')[1])

for i in s:
    print(i)
'''***********************************************'''

data=readData("D:\\spark performance\\questions_sub.txt")
orderid=5

def sumOfFields(data,orderid):
    s=0.0
    for i in data:
        if(int(i.split(',')[0])== orderid):
            s+=float(i.split(',')[6])

    return s

sums=sumOfFields(data,orderid)
print(sums)

'''***********************************************'''

data=readData("D:\\spark performance\\questions_sub.txt")
def sumPerItems(data):
    sums_order={}
    for i in data:
        #print(i.split(',')[0])
        sumTuple=(int(i.split(',')[0]),int(i.split(',')[6]))
        #print(sumTuple)
        if(sums_order.get(sumTuple[0])):
            sums_order[sumTuple[0]]+=sumTuple[1]
        else:
            sums_order[sumTuple[0]]=sumTuple[1]

    return sums_order

print(sumPerItems(data))
'''*************************************************'''

def getTags(data):
    data_list=[]
    for i in data:
      if(i.split(',')[1] in ('html','c#','mysql')):
          data_list.append(i)
    return data_list

data=readData("D:\\spark performance\\question_tags.csv")
data2=getTags(data)

def getDictFromData(data):
    datadict={}

    for i in data:
        dataAttribute=i.split(',')
        if(dataAttribute[1] in ('html','c#','mysql')):
            datadict[dataAttribute[0]]=dataAttribute[1]
    return datadict

print(getDictFromData(data))











