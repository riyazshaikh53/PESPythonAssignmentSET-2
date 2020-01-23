list1 = [10,45,78,42,65,41]
list2 = [12,4,5,7,8,21]
list3 = [1,5,75,7,56,4]
maxlist = []
minlist = []
sum1=sum2=0

print(list1)
print(list2)
print(list3)

list1.sort()
list2.sort()
list3.sort()

n1 = len(list1)
n2 = len(list2)
n3 = len(list3)

maxlist.append(list1[n1-1])
maxlist.append(list1[n1-2])
maxlist.append(list2[n2-1])
maxlist.append(list2[n2-2])
maxlist.append(list3[n3-1])
maxlist.append(list3[n3-2])

minlist.append(list1[0])
minlist.append(list1[1])
minlist.append(list2[0])
minlist.append(list2[1])
minlist.append(list3[0])
minlist.append(list3[1])

print("MAXLIST :")
print(maxlist)
print("MINLIST :")
print(minlist)


for i in range(len(minlist)):
    sum1 += minlist[i]
    sum2 += maxlist[i]

Avg1 = sum1/len(minlist)
Avg2 = sum2/len(maxlist)

print("Average of MAXLIST :",Avg2)
print("Average of MINLIST :",Avg1)
