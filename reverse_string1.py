def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]

input_string = input('Enter the string: ')
print('input string:', input_string)
print("The reversed string is : ", end="")
print(reverse(input_string))