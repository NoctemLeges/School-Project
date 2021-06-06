l = eval(input("Enter a list:"))

l_rev = []
l_swapped_halves = []
freq_dict = {}

# reversing the list
for i in range(-1, -len(l)-1,-1):
    l_rev.append(l[i])
print("Reverse list",l_rev)
#______________________________________________

#displaying frequency
for i in l:
    freq_dict[i] = l.count(i)

print("Number \t Frequency")
for key,value in freq_dict.items():
    print("%d \t %d" %(key,value))
#_______________________________________________

#swapping halves

if len(l)%2 ==0:
    half1 = l[ :len(l)//2]
    half2 = l[len(l)//2: ]
    
    l_swapped_halves = half2 + half1
    print(l_swapped_halves)
elif len(l)%2 !=0:
    half1 = l[ :len(l)//2]
    half2 = l[len(l)//2+1: ]
    l_swapped_halves = half2 + half1
    l_swapped_halves.insert(len(l)//2,l[len(l)//2])
    print(l_swapped_halves)
#_________________________________________________




