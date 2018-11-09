s=str(input("enter th string"))
rev_str = reversed(s)
if list(s) == list(rev_str):
   print("It is palindrome")
else:
   print("It is not palindrome")