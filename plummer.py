# Problem: Calculate plumber’s bill.

# Input:  minutes worked

# Input: True if urgent, False otherwise

# Output:  cost

minutes = 61

urgent = False

cost = 0

hours = 1

if minutes > 60 :

    hours = minutes // 60

if minutes % 60 == 0 :
    hours = minutes // 60 - 1

if urgent:

    cost = 200 + hours * 80

if not urgent:

    cost = 100 + hours * 50

print(cost)
