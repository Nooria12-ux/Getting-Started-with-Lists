start = int(input("Enter the starting point: "))
end = int(input("Enter the ending point: "))

sqlist = []
even = []
odd = []

for i in range(start, end + 1):
    square = i ** 2  
    sqlist.append(square)  
    
    if square % 2 == 0:
        even.append(square)
    else:
        odd.append(square)

print(f"\nThe list of square values: {sqlist}")
print(f"The even numbers are: {even}")
print(f"The odd numbers are: {odd}")