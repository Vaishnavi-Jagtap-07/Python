s1=input(" Enter any string : ")
s2=input(" enter any string : ")
c1=0
c2=0
for i in s1:
  if i in s2:
    c1+=1
for i in s2:
  if i in s1:
    c2+=1
if (c1==len(s2)) and (c2==len(s1)):
   print("\nIt is Anagram")
else:
    print("\nIt is not Anagram")
