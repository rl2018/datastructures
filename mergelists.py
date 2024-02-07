list1=[2,5,15,36,47,56,59,78,156,244,268]
list2=[18,39,42,43,66,69,100]

counter=1
i1=0
i2=0
maxi1=len(list1)
maxi2=len(list2)
mergedList=[]
while counter<(len(list1)+len(list2)):
    if i1<maxi1 and i2<maxi2:
        if list1[i1]>list2[i2]:
            mergedList.append(list2[i2])
            print(mergedList)
            counter+=1
            i2+=1
        elif list1[i1]<list2[i2]:
            mergedList.append(list1[i1])
            print(mergedList)
            counter+=1
            i1+=1
        elif list1[i1]==list2[i2]:
            mergedList.append(list1[i1])
            mergedList.append(list2[i2])
            print(mergedList)
            counter+=2
            i1+=1
            i2+=1

print(mergedList)