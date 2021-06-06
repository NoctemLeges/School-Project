l = eval(input("Enter a list: "))
l.sort()
l_fixed = []
freq_dict={}
ds = set()
#Second maximum element
for i in l:
    if i not in l_fixed:
        l_fixed.append(i)
print("The second maximum number is", l_fixed[-2])
#_____________________________________________________
    
#Duplicate numbers
for i in l:
    if l.count(i)>1:
        ds.add(i)
print(list(ds))
#_____________________________________________________

#Maxumum frequency
for i in l:
    freq_dict[i] = l.count(i)
m = max(list(freq_dict.values()))

for i in freq_dict:
    if freq_dict[i]==m:
        print("Number",i,"has highest frequency which is",m)        
#________________________________________________________



