s1=str(int(input(" Enter any string : ")))
b=0

for i in s1:
   b=b+int(i)**len(s1)
if  int(s1)==b:
  print("\nIt is armstrong number")
else:
  print(" \nIt is not armstrong number")
