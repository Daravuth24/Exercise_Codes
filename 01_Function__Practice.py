# 1. Create a function to input the weather in celsius and convert it to fahrenheit
# 2. Create a function to input the weather in fahrenheit and convert it to celsius
# 3. Create a function that accepts name as the argument and prints the middle character of the name
# 4. Create a function that receives and array(list) and search element(number to be found from the array)
# The function must return the position of the search number of the array if the search number is not available
# in the array then return "Element not found in the array!".

def celTofah():
    cel = int(input("Input the weather in celsius:"))
    fah = cel*9/5 +32
    print(f"The weather in fahrenheit:{fah}")
# celTofah()

def fahTocel():
    fah = int(input("Input the weather in fahrenheit:"))
    cel = (fah-32) *5/9
    print(f"The weather in celsius:{cel}")
# fahTocel()

def midchar(name):
    mid = len(name)//2
    print(f"The middle character of your name: {name[mid]}")

celTofah()
fahTocel()
midchar("Chheang")
