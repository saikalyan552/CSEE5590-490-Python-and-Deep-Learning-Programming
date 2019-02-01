total = int(input(" total number of plants "))
print("enter heights of plants")
sum  = 0.0
b = [int(x) for x in input().split()]
for a in b:
    sum = sum + a
print("\n The average  of the numbers  is", round(sum / total,3))