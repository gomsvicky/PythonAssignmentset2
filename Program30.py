list1 = []
num = input("Enter number of elements in list: ")
num = int(num)

for i in range(1, num + 1):
    ele = input("Enter elements: ")
    list1.append(ele)
print("Entered elements ", list1)

new_list = []
while list1:
    minimum = list1[0]
    for x in list1:
       if x < minimum:
        minimum = x
    new_list.append(minimum)
    list1.remove(minimum)

print("After sorting the entered elements : ", new_list)