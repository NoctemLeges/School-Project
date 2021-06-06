s = input("Enter a sentence")
len_dict = {}
l = s.split()
count = 0
result = ""
#Arranging
for w in l:
    len_dict[w] = len(w)
l_sorted = list(len_dict.values())
l_sorted.sort()

for i in l_sorted:
    for w in len_dict:
        if len_dict[w] ==i:
            result+=w + " "
print(result)
#___________________________________________
# Vowel checking
for w in l:
    if w[0] in ['a','e','i','o','u','A','E','I','O','U']:
        count+=1
print("No of words:",count)
#_________________________________________________
