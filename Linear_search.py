#write the code for linear search taking user input
def LS(arr, item):
    for i in range(len(arr)):
        if arr[i] == item:
            return i  
    return -1  
arr = input("Enter a list of numbers without tapping enter :: ").split()
arr = [int(x) for x in arr]
item = int(input("Enter the number to search for: "))
rst = LS(arr, item)
if rst != -1:
    print(f"{item} found at index {rst}.")
else:
    print(f"{item} not found in the list.")
