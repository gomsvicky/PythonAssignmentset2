list1 = ['Namakkal', 'Coimbatore', 'Salem', 'Trichy', 'Erode']
list2 = ['Chennai', 'Delhi', 'Pune', 'Hyderabad', 'Mysore']
list3 = ['Bangalore', 'Hosur', 'Dindigul', 'Kanchipuram', 'Ooty']
length1 = [len(list1[0]), len(list1[1]), len(list1[2]), len(list1[3]), len(list1[4])]
length2 = [len(list2[0]), len(list2[1]), len(list2[2]), len(list2[3]), len(list2[4])]
length3 = [len(list3[0]), len(list3[1]), len(list3[2]), len(list3[3]), len(list3[4])]
print("length of list1 is ", length1)
print("length of list2 is ", length2)
print("length of list3 is ", length3)

i = 0
while i < len(list1):
    print("city name is ", str(list1[i]) + " and its length is", str(length1[i]))
    print("city name is ", str(list2[i]) + " and its length is", str(length2[i]))
    print("city name is ", str(list3[i]) + " and its length is", str(length3[i]))
    i += 1

max1 = max(length1)
min1 = min(length1)
max2 = max(length2)
min2 = min(length2)
max3 = max(length3)
min3 = min(length3)

if max1 > max2 and max1 > max3:
    print("maximum length is ", max1)
elif max2 > max1 and max2 > max3:
    print("maximum length is ", max2)
else:
    print("maximum length is ", max3)

if min1 < min2 and min1 < min3:
    print("Minimum length is ", min1)
if min2 < min1 and min2 < min3:
    print("Minimum length is ", min2)
else:
    print("Minimum length is ", min3)


print("list 1 items", list1)
list1.pop(0)
list1.pop(-1)
print("List after first and last item deleted", list1)

print("list 2 items", list2)
list2.pop(0)
list2.pop(-1)
print("List after first and last item deleted", list2)

print("list 3 items", list3)
list3.pop(0)
list3.pop(-1)
print("List after first and last item deleted", list3)
