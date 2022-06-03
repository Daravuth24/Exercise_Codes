def l_search(nums_list, search_no):
    index = 0
    while index < len(nums_list):
        if nums_list[index] == search_no:
            return index+1
        index += 1
    else:
            return -1

my_list = [10, 20, 30, 40]
sno = int(input("Search:"))
element_position = l_search(my_list, sno)

if element_position == -1:
    print("Element not found in the list")
else:
    print(f"Element found at: {element_position}")