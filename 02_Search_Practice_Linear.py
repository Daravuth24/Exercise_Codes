def l_search(nums_list, search_no):
   while True:
       if search_no in nums_list:
           return f"Element Found: {nums_list.index(search_no)+1}"
       else:
           return "Element not found"

my_list = [10,20,30,40,50]
sno = int(input("Element want to search: "))
element_position = l_search(my_list, sno)
print(element_position)