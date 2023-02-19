def reverse_string(str1):
    reverse_str = ""
    index = len(str1)
    while index > 0:
        reverse_str = reverse_str + str1[index - 1]
        index = index - 1
    return reverse_str
Output = reverse_string('1234abcd')
print(Output)