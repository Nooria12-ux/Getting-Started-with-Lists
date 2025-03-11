l = [4,5,1,2,9,7,10,8]
print(f"Original list : {l}")

sum = 0
for i in l:
    sum = sum + 1
    
print(f"sum = {sum}")

avg = sum / len(l)
print(f"average = {avg}\n\n")

l.sort()
print(f"Sorted list: {l}")

print(f"Smallest element is : {l[0]}")
print(f"Largest element is : {l[-1]}")