dic1 = {
    "name" : "Goms",
"ID" : "123456",
"status" : "Active"
}
dic2 = {
    "age" : 27,
    "year" : 1991,
    "month" : "September"
}
dic3 = {
    "location" : "Bangalore",
    "husband" : "Vignesh",
    "Marriage" : True
}
print("Comparison operator is not supported in Python 3")
print("Dictionary 1 :", dic1)
print("Dictionary 2 :", dic2)
print("Dictionary 3 :", dic3)
dic1["Band"] = "Rainbow"
dic2["date"] = 4
print("Dictionary 1 after adding new entry:", dic1)
print("Dictionary 2 after adding new entry:", dic2)
print("Length of dic 1 :", len(dic1))
print("Length of dic 2 :", len(dic2))
print("Length of dic 3 :", len(dic3))
final = str(dic1) + str(dic2) + str(dic3)
print("Converted all dictionaries as string and concatenate all strings together")
print(final)