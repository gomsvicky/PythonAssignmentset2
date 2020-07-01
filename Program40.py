import time
i = 12
while i > 0:
    print(time.asctime())
    time.sleep(5)
    i -=1
start = time.asctime()
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
end = time.asctime()
print("Start program at ", start, " and end at ", end)