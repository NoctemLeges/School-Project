s = input("Enter a word:")
vowels = ['a','e','i','o','u','A','E','I','O','U']
v = 0
cons = 0
l = []
freq_dist ={}
for c in s:
    l.append(c)
    if c in vowels:
        v+=1
    elif c.isalpha():
        cons+=1
for i in l:
    freq_dist[i] = l.count(i)
for key,value in freq_dist.items():
    print(key + '-' + str(value))
print("Vowels-", v)
print("consonants-", cons)
