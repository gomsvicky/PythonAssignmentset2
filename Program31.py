list1 = []
num = input("Enter number of elements in list: ")
num = int(num)

for i in range(1, num + 1):
    ele = int(input("Enter elements: "))
    list1.append(ele)
print("Entered elements ", list1)

searchnum = int(input("Enter a number to search in above list : "))
found = 0
for j in list1:
    if j == searchnum:
        print("success")
        found = 1
        break
if found == 0:
    print("un successful search")