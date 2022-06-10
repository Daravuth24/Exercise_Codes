def bSearch(numlist, sno):
    beg = 0
    end = len(numlist)-1
    for i in range(0, len(numlist)):
        mid = (beg+end)//2
        if numlist[mid] == sno:
            return mid
        elif numlist[mid] < sno:
            end = mid - 1
        else:
            beg = mid + 1
    else:
        return -1

pos = bSearch([999, 700, 600, 500, 400, 300, 42], 400)
message = "Element not found"
if pos != -1:
    message=f"ELement found at: {pos+1}"
print (message)