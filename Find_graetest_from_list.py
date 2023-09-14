# wap to find a max from a list of numbers
numbers = [int(x) for x in input("Enter a list of numbers:: ").split()]
max_no = numbers[0]
for num in numbers:
    if num > max_no:
        max_no = num
print(f"The maximum number is: {max_no}")
