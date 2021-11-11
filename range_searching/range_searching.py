nums = [1, 1, 1, 3, 5, 1, 7]
target = 1

def find_num(nums, target):
    index_list = []
    for number in range(len(nums)):
        if target in nums:
            index_list = [x for x in range(len(nums)) if nums[x] == target]
            res = [ index_list[0], index_list[-1] ]
            return (str(res))
            break
        else:
            return ([-1, -1])
            break

print(find_num(nums, 3))
