#Create two lists. The first list should consist of odd numbers. The second list is also of even numbers.
#Merge these two lists. Multiply all values in the new list by 2.
# Use a loop to print the data type of the values in the new list.

nums = list(range(5))
odd_squares = [i**3 for i in nums if i% 2 == 1]
print(odd_squares)

nums = list(range(4))
even_squares = []

for i in nums:
  even_squares.append(i*2)
print(even_squares)

list1 = ([even_squares] + [odd_squares])

list3 = [a*2 for a in (list1)]
print(list3)

while True:
    a = input("Enter a list: ")
    if a == "list3":
        print(type(list3))
