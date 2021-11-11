nums = [1, 2, 3, 8, 9, 10]

import itertools

def findSmallest(nums):
    all_combinations = []
    sum_list = []
    for r in range(len(nums) + 1):
        # Call itertools.combinations(iterable, r) with a list as iterable to return a combinations object containing 
        #all combinations of the list that have length r.
        # taken from here: https://www.kite.com/python/answers/how-to-find-all-combinations-of-a-list-in-python
        combinations_object = itertools.combinations(nums, r)
        combinations_list = list(combinations_object)
        # all_combinations is the list of possible combinations of any subset in the list
        all_combinations += combinations_list
      for values in range (0, len(all_combinations)):  
        # here we iterate over that list of tuples and append the sum of each element to sum_list
        sum_list.append(sum(all_combinations[values]))
    for i in range(1, max(sum_list)):
        # here we define a range from 1 to the max of the sum_list and start counting from 1. If not, it prints the value.
        # other solutions here: https://stackoverflow.com/questions/28176866/find-the-smallest-positive-number-not-in-list
        if i not in sum_list: break
    print (all_combinations)
    print()
    print(set(sum_list))
    print()
    return i

print (findSmallest([1, 2, 3, 8, 9, 10]))
