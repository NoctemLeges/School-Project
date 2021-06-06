l1 = eval(input("Enter the first list:"))
l2 = eval(input("Enter the second list:"))


u =[]
ir=[]
max = l1

if(len(l2)>len(l1)):
    max = l2
print("The list with maximum number of elements is ",max)

for i in l1:
    if i not in u:
        u.append(i)
for i in l2:
    if i not in u:
        u.append(i)
print("The union is ",u)

for num in l1:
    if num in l2:
        ir.append(num)
print("The intersection of the two lists in", ir)

