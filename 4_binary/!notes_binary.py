# To get better times, you want to process more bits at once or use a cache table

# To erase the lowest set bit:
x = 0
x &= (x - 1)
# This works because minusing one causes at least one 1 to appear in a place where there are guaranteed only 0s

# To isolate the lowest set bit:
x &= ~(x - 1)

# XOR of all 1's flips every bit
# XOR of all 0's does nothing
# XOR two numbers, the result is addition without carries

# & AND two numbers, the result is the carry

# Create masks by putting 1's in what you have to preserve, 0's in what you don't, and &ing
