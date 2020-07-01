list1 = ['Namakkal', 'Coimbatore', 'Salem', 'Trichy', 'Erode']
list1.append("Ooty")
print("Appended one item ", list1)
list1.insert(4, "Bangalore")
print("inserted 4th index with Bangalore ", list1)
list1.sort()
print("The order after sorting ", list1)
list1.reverse()
print("descenting order of list", list1)
i = 0
while i < 3:
    list1.pop()
    i +=1
print("Removed last 3 items from the list ", list1)