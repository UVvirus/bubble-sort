list1=[42,34,0,24,4]
for j in range(len(list1)-1):
    for i in range(len(list1)-1-j):#(-j is used for (no need to compare sorted elements)i.e,for efficiency )
     if list1[i]>list1[i+1]:
        list1[i],list1[i+1]=list1[i+1],list1[i]

print(list1)