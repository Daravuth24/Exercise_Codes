
def finding_an_element_in_array(arr, numtosearch):
    for i in range (0, len(arr)):
        if arr[i] == numtosearch:
            return f"Element found at index {i}"
    return "Element not found in the array!"

result = finding_an_element_in_array([54,45,78,98,56], 78)
print(result)

