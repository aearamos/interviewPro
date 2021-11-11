import itertools
def generateAllSubsets(nums):
    all_combinations = []
    for r in range(len(nums) + 1):
        combinations_object = itertools.combinations(nums, r)
        combinations_list = list(combinations_object)
        all_combinations += combinations_list
    return set(all_combinations)

print(generateAllSubsets([1, 2, 3]))
