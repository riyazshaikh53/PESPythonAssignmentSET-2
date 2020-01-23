tup1 = ("Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday")
print(tup1)
tup2 = ("January","February","March","April","May","June","July","August","September","October","November","December")
print(tup2)

tup1 = tup1 + tup2
print(tup1)

tup1 = (10,25,41,24,15,11)
tup2 = (15,47,85,96,24,66)
tup3 = (16,21,45,14,67,18)

print(tup1)
print(tup2)
print(tup3)

sum1=sum2=sum3=0

n = len(tup1)

for i in range(n):
    sum1+=tup1[i]
    sum2+=tup2[i]
    sum3+=tup3[i]

print(sum1)
print(sum2)
print(sum3)


if(sum1>sum2 and sum1>sum3):
    print("Maximum Tuple :Tuple1")

if(sum2>sum1 and sum2>sum3):
    print("Maximum Tuple :Tuple2")

if(sum3>sum2 and sum3>sum1):
    print("Maximum Tuple :Tuple3")

list1=list(tup1)
list1.append(54)
tuple1 = tuple(list1)
print("Adding new element in the tuple by typecasting it to list :")
print(tuple1)

list1.remove(54)
tuple1 = tuple(list1)
print("Removing an element in the tuple by typecasting it to list :")
print(tuple1)
