s = input("Enter a sentence:")
length_dict = {}
l = s.split()
count = 0
for w in l:
    length_dict[w] = len(w)
    if w == w[::-1] and len(w)>1:
        count +=1
print("Number of palindrome words =",count)
m = max(list(length_dict.values()))
print("The longest word/s are:")
for w in l:
    if len(w)==m:
        print(w)

