def display_sums(numbers):
    """
    Display pairs of numbers that sum to 10 using a set in O(n) time
    We are assuming that there are no duplicates in the list
    """
    values_seen = set()
    for n in numbers:
        # If 10-n is in the values_seen set then I know that
        # I have previously seen a number that will sum with n
        # to equal 10.  Display that pair
        if 10-n in values_seen:
            print(n, 10-n)
        # Add this number to the values_seen set
        values_seen.add(n)


display_sums([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 6])
"""
Should show something like (order does not matter):
6 4
7 3
8 2
9 1
10 0
6 4
"""
print("===========")
display_sums([-30, -25, -20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30])
"""
Should show something like (order does not matter):
10 0
15 -5
20 -10
25 -15
30 -20
"""
print("===========")
display_sums([4, 3, 5, 11, 2, -4, 6, 8, -1, -3, -2])
"""
Should show something like (order does not matter):
6 4
8 2
-1 11
"""
