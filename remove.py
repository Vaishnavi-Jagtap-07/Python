str1=input("Enter any sentence : ")
m=input("enter character from above to remove :")
new=''
for i in str1:
  if i!=m:
    new=new+i
print("\nWe get")
print(new)
