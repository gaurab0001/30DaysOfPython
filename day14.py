# Day 14 of 30 Days Python Challenge
# Topic: Sets in Python

# Creating sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Set operations
print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference (set1 - set2):", set1 - set2)
print("Symmetric Difference:", set1 ^ set2)

# Adding and removing elements
set1.add(10)
set1.discard(2)
print("Updated set1:", set1)
