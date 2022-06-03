def b_search(nums_list, sno):
    beg = 0
    end = len(nums_list)-1
    for i in range(0, len(nums_list)):
        mid = (beg + end)//2
        if nums_list[mid] == sno:
            return mid
        elif nums_list[mid] < sno:
            end = mid - 1
        else:
            beg = mid + 1
    else:
        return -1

pos = b_search([999, 897, 656, 542, 300, 125, 75, 9], 300)
message = "Element not found in the list"
if pos != -1:
    message = f"Element found at position: {pos + 1}"
print(message)
