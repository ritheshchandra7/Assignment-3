def sum1(numbers):
    total = 0
    for x in numbers:
        total += x
    return total

input_string = input('Enter elements of the list separated by space ')
print("\n")
user_list = input_string.split()

for i in range(len(user_list)):
    user_list[i] = int(user_list[i])

print('Given list: ', user_list)

print("Sum = ", sum1(user_list))