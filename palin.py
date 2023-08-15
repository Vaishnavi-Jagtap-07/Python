s1=input("Enter any string : ")
rev=''
for i in s1:
    rev=i+rev
if rev==s1:
  print("\nIt is Palindrome")
else:
  print("\nIt is not Palindrome")
