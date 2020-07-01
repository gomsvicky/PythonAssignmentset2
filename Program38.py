dic1 = {
    'Name': 'Ramakrishna',
     'Age': 25
}
dic2 = {
    'EmpId': 1234,
     'Salary': 5000
}
dic1.update(dic2)
print("Dictionary 1 has been updated with all the values in dic 2 \n", dic1)
dic1["Salary"] = 5500
print("Salary has been increased to 10% \n", dic1)
dic1["Age"] = 26
print("Age has been updated to 26 \n", dic1)
dic1["Grade"] = "B1"
print("Inserted new value \n", dic1)
print("Only keys \n", dic1.keys())
print("Only Values \n", dic1.values())
del dic1["Age"]
print("Deleted Age and the result is \n", dic1)