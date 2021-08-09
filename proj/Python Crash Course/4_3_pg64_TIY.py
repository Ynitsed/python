# Page 64
print("\n------------------------------------------\n")

#4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.
print("4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.\n")
value = [value for value in range(1,21)]
print(value)
print("\n------------------------------------------\n")

#4-4. One Million: Make a list of the numbers from one to one million, 
#and then use a for loop to print the numbers . (If the output is taking too long, 
# stop it by pressing ctrl-C or by closing the output window .)
print("4-4. One Million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers . (If the output is taking too long, stop it by pressing ctrl-C or by closing the output window .\n")
value = [value for value in range(1,10**6+1,100000)]
print(value)
print("\n------------------------------------------\n")

#4-5. Summing a Million: Make a list of the numbers from one to one million, 
# and then use min() and max() to make sure your list actually starts at one 
# and ends at one million . Also, use the sum() function to see how quickly Python 
# can add a million numbers .
print("4-5. Summing a Million: Make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually starts at one and ends at one million . Also, use the sum() function to see how quickly Python can add a million numbers .\n")
list = [ value for value in range(1, 10**6+1)]
print(min(list))
print(max(list))
print(sum(list))
print("\n------------------------------------------\n")

#4-6. Odd Numbers: Use the third argument of the range() function 
# to make a list of the odd numbers from 1 to 20 . Use a for loop 
# to print each number .
print("4-6. Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20 . Use a for loop to print each number .\n")
print([odd_number for odd_number in range(1,20,2)])
print("\n------------------------------------------\n")

#4-7. Threes: Make a list of the multiples of 3 from 3 to 30 . 
# Use a for loop to print the numbers in your list .
print("4-7. Threes: Make a list of the multiples of 3 from 3 to 30 . Use a for loop to print the numbers in your list .\n")
print([threes for threes in range(3,31,3)])
print("\n------------------------------------------\n")

#4-8. Cubes: A number raised to the third power is called a cube . 
# For example, the cube of 2 is written as 2**3 in Python . 
# Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), 
# and use a for loop to print out the value of each cube .
print("4-8. Cubes: A number raised to the third power is called a cube . For example, the cube of 2 is written as 2**3 in Python . Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube .\n")
print([cube**3 for cube in range(1,11)])
print("\n------------------------------------------\n")

#4-9. Cube Comprehension: 
# Use a list comprehension to generate a list of the first 10 cubes .
print("4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes .\n")
print([cube**3 for cube in range(1,11)])
print("\n------------------------------------------\n")