
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    print(nums)
    dict = {}
    for i in range ( len ( nums ) ):
        print('position:',str(i),'value:',nums[i])
        if target - nums[i] not in dict:
            dict[nums[i]] = i
            print ( 'generated dict:',dict )
        else:
            print('answer',[dict[target - nums[i]],i])

    print('final dict',dict)
twoSum([3,3],6)