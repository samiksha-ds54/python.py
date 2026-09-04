# Array implementation and searching

# Create an array (list)
arr = [10, 20, 30, 40, 50, 60, 70]

print("Array:")
print(arr)

# Take element to search
key = int(input("\nEnter element to search: "))

# ---------------- LINEAR SEARCH ----------------
found = False

for i in range(len(arr)):
    if arr[i] == key:
        print("\nLinear Search:")
        print("Element found at index:", i)
        found = True
        break

if not found:
    print("\nLinear Search:")
    print("Element not found")


# ---------------- BINARY SEARCH ----------------
low = 0
high = len(arr) - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == key:
        print("\nBinary Search:")
        print("Element found at index:", mid)
        found = True
        break
    elif arr[mid] < key:
        low = mid + 1
    else:
        high = mid - 1

if not found:
    print("\nBinary Search:")
    print("Element not found")