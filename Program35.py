tup1 = ("Monday", "Tuesday", "Wednessday", "Thursday", "Friday", "Saturday", "Sunday")
for i in tup1:
    print(i)
tup2 = ("Jan", 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
print(tup1 + tup2)
tup1 = (1, 5, 9, 3, 7)
tup2 = (4, 8, 2, 10, 6)
tup3 = (16, 12, 18, 14, 15)
if tup1 > tup2 and tup1 > tup3:
    print("tup1 is greater")
elif tup2 > tup1 and tup2 > tup3:
    print("tup2 is greater")
else:
    print("Tup3 is greater")

print("Tuple list ", tup1)
tup1 = tup1[1:]
print("After deleting a element in tuple ", tup1)
del tup1
print(tup1)
tup1 = tup2
print("Current tuple values ", tup1)
list1 = list(tup1)
list1.append(55)
tup1 = tuple(list1)
print("Appended a value in tuple using typecasting ", tup1)