# Page 61
#numbers
print("\n------------------------------------------\n")
for value in range(1,5):
    print(value)

print("\n------------------------------------------\n")

numbers = list(range(1,6))
print(numbers)

print("\n------------------------------------------\n")

even_numbers = list(range(2,11,2))          #even_numbers
print(even_numbers)                         

print("\n------------------------------------------\n")

squares = []
for value in range(1,11):                   #squares
    square = value**2                       
    squares.append(square)                  

print(squares)

print("\n------------------------------------------\n")

squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)

print("\n------------------------------------------\n")

digits = []                                 #max, min, sum
for value in range(0,10):
    digits.append(value)
print(digits)
print(min(digits))
print(max(digits))
print(sum(digits))

print("\n------------------------------------------\n")

squares = [value**2 for value in range(1,11)]
print(squares)

print("\n------------------------------------------\n")