def threeSumClosest(nums: list[int], target: int) -> int:
    """
    :type nums: List[int]
    :type target: int
    :return: int
    """
    n = len(nums)
    closest_sum = float('inf')
    
    # 首先对nums列表进行排序
    nums.sort()
    
    for i in range(n):
        left = i + 1
        right = n - 1
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            diff = abs(current_sum - target)
            
            # 更新最接近的和以及差的平方
            if diff < closest_sum:
                closest_sum = diff
            if current_sum == target:
                break
            
            if current_sum < target:
                left += 1
            else:
                right -= 1
    
    return closest_sum
print(threeSumClosest(nums = [-1,2,1,-4], target = 1))
