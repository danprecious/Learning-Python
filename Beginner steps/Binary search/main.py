# let's say we have a sorted array
sorted_list = [1, 3, 6, 15, 20, 23, 25, 28, 30, 33, 36, 39, 42, 46, 50, 53]


# we need to locate the right and left points; the starting and ending.
def binary_search(list, target):
    left, right = 0, len(list) - 1

    # we want to find the midpoint of the collection or list
    while left <= right:
        mid = left + (right - left) // 2
        if list[mid] == target:
            return mid
        elif list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1


print(binary_search(sorted_list, 53))

left, right = 0, len(sorted_list) - 1
mid = left + (right - left) // 2
print(mid)
