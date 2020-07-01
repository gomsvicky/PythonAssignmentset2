string = input("Enter a text : ")
string = string.lower()
ovals = 'aeiou'
count = {}.fromkeys(ovals, 0)

for c in string:
    if c in count:
        count[c] +=1
print(count)
