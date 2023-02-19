def fun(str1):
  upper_case = 0
  lower_case = 0
  for i in str1:
    if i.isupper():
      upper_case += 1 
    elif i.islower():
      lower_case += 1
    else:
      pass
  print("Original string:", str1)
  print("No. of Upper case characters:", upper_case)
  print("No. of Lower case characters:", lower_case)
fun("The quick Brow Fox")