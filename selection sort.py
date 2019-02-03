li=[54,34,3,4,2,0]
print(li)
min_val=min(li)
min_ind=li.index(min_val)
li[0],li[min_ind]=li[min_ind],li[0]
print(li)

for i in range(len(li)):
    min_val=min(li[i:])
    min_ind=li.index(min_val)
    li[i],li[min_ind]=li[min_ind],li[i]
print(li)
