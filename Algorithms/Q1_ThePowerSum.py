# Generate a list of (1...n)^pwr in main function
#
# In helper, we try to hit 0.
#  - We subtract the last element (biggest), then recurse
#    - If num < 0, we went too negative. Stop path w/ ret 0
#    - If num == 0, then return that we found the combo
#    - Else recurse
#  - Also 2nd path. Ignore the largest element, recurse without sub. This lets us use the 2nd, 3rd, 4th, ... largest elements.

def helper(num, array):
    # Total combos found
    total = 0
    
    # Hit the desired number
    if num == 0:
        total += 1
    # Overshot
    elif num < 0:
        pass
    # Empty array
    elif not array:
        pass
    else:
        total += helper(num, array[:-1]) + helper(num - array[-1], array[:-1])
    
    return total

def get_num_combos(num, pwr):
    # Get max for range by taking the pwr root
    max_range = int(num ** (1.0/pwr))
    
    # Make list, then reverse it
    ary = [x**pwr for x in range(1,max_range+1)]
    #ary = ary[::-1]
    
    return helper(num, ary)
    
final = int(input())
power = int(input())

print(get_num_combos(final, power))
