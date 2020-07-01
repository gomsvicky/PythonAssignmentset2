list1 = [1, 5, 9, 3, 7]
list2 = [4, 8, 2, 10, 6]
list3 = [16, 12, 18, 14, 15]
list1.sort()
list2.sort()
list3.sort()
print("List of elements \n", list1, "\n", list2, "\n", list3)
max1 = []
max1.append(list1[-1])
max1.append(list1[-2])
max1.append(list2[-1])
max1.append(list2[-2])
max1.append(list3[-1])
max1.append(list3[-2])
max1.sort()
print("Formed max list from all 3 lists ", max1)
avg = sum(max1)/len(max1)
print("Average of maxlist:", avg)
min1 = []
min1.append(list1[1])
min1.append(list1[0])
min1.append(list2[1])
min1.append(list2[0])
min1.append(list3[1])
min1.append(list3[0])
min1.sort()
print("Formed Min list from all 3 lists ", min1)
avg1 = sum(min1)/len(min1)
print("Average of minlist:", avg1)